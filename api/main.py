from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
import time
from typing import List, Dict, Any, Optional

OLLAMA_HOST = "http://127.0.0.1:11434"

# Esquema de petición para generar un prompt
class RunRequest(BaseModel):
    model: str
    prompt: str

class BatchTestRequest(BaseModel):
    models: List[str]
    problem_ids: Optional[List[str]] = None  # If None, test all problems

class TestResult(BaseModel):
    problem_id: str
    model: str
    prompt: str
    response: str
    time_ms: int
    language: str

app = FastAPI(
    title="API Proyecto LLM",
    description="Servicio que envuelve Ollama para ejecutar prompts",
    version="0.1.0"
)

@app.get("/models")
def list_models():
    """Lista los modelos disponibles en Ollama."""
    try:
        resp = requests.get(f"{OLLAMA_HOST}/v1/models")
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/run")
def run_prompt(req: RunRequest):
    """Ejecuta un prompt con un modelo y devuelve la respuesta."""
    payload = {
        "model": req.model,
        "messages": [{"role": "user", "content": req.prompt}]
    }
    try:
        resp = requests.post(
            f"{OLLAMA_HOST}/v1/chat/completions",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        resp.raise_for_status()
        data = resp.json()
        # Extraer el contenido de la primera respuesta
        content = data["choices"][0]["message"]["content"]
        return {"response": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/problems")
def list_problems():
    """Lista todos los problemas disponibles para testing."""
    try:
        prompts_dir = "../prompts"  # Ruta relativa a donde se ejecuta la API
        problems = []
        
        # Process both language directories
        for lang in ["espanol", "ingles"]:
            lang_dir = os.path.join(prompts_dir, lang)
            if not os.path.exists(lang_dir):
                continue
                
            for file in os.listdir(lang_dir):
                if file.startswith("benchmark_ej") and file.endswith(".txt"):
                    problem_id = file.replace(".txt", "")
                    with open(os.path.join(lang_dir, file), "r") as f:
                        content = f.read().strip()
                    problems.append({
                        "id": problem_id,
                        "content": content,
                        "language": lang
                    })
        
        return {"problems": sorted(problems, key=lambda x: x["id"])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/batch-test")
def batch_test(req: BatchTestRequest):
    """Ejecuta un lote de problemas en múltiples modelos y devuelve los resultados."""
    try:
        # Obtener la lista de problemas
        prompts_dir = "../prompts"
        results = []
        
        # Process each model and problem combination
        for model in req.models:
            # Process both language directories
            for lang in ["espanol", "ingles"]:
                lang_dir = os.path.join(prompts_dir, lang)
                if not os.path.exists(lang_dir):
                    continue
                    
                if req.problem_ids:
                    problem_files = [f"benchmark_ej{id.split('benchmark_ej')[-1]}.txt" 
                                    if id.startswith("benchmark_ej") else f"benchmark_ej{id}.txt" 
                                    for id in req.problem_ids]
                else:
                    problem_files = [f for f in os.listdir(lang_dir) 
                                    if f.startswith("benchmark_ej") and f.endswith(".txt")]
                
                for file in problem_files:
                    problem_path = os.path.join(lang_dir, file)
                    if not os.path.exists(problem_path):
                        continue
                    
                    try:
                        with open(problem_path, "r") as f:
                            prompt = f.read().strip()
                        
                        # Ejecutar el prompt y medir tiempo
                        start_time = time.time() * 1000
                        payload = {
                            "model": model,
                            "messages": [{"role": "user", "content": prompt}]
                        }
                        
                        # Add timeout and retry logic
                        max_retries = 3
                        retry_delay = 5  # seconds
                        
                        for attempt in range(max_retries):
                            try:
                                resp = requests.post(
                                    f"{OLLAMA_HOST}/v1/chat/completions",
                                    json=payload,
                                    headers={"Content-Type": "application/json"},
                                    timeout=180  # 3 minutes timeout per request
                                )
                                resp.raise_for_status()
                                data = resp.json()
                                break
                            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                                if attempt == max_retries - 1:
                                    raise
                                time.sleep(retry_delay)
                        
                        end_time = time.time() * 1000
                        
                        # Extraer el contenido de la respuesta
                        content = data["choices"][0]["message"]["content"]
                        problem_id = file.replace(".txt", "")
                        
                        results.append(TestResult(
                            problem_id=problem_id,
                            model=model,
                            prompt=prompt,
                            response=content,
                            time_ms=int(end_time - start_time),
                            language=lang
                        ))
                    except Exception as e:
                        # Log the error but continue with other problems
                        print(f"Error processing {file} with model {model}: {str(e)}")
                        continue
        
        return {"results": [r.dict() for r in results]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
