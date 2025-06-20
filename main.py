from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess

app = FastAPI(title="GPT DevOps API", version="1.0.0")

class CommandRequest(BaseModel):
    command: str

@app.get("/")
def read_root():
    return {"message": "API GPT DevOps Builder rodando!"}

@app.post("/execute")
def execute_command(req: CommandRequest):
    try:
        result = subprocess.check_output(req.command, shell=True, stderr=subprocess.STDOUT)
        return {"output": result.decode()}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail=e.output.decode())

@app.get("/health")
def health():
    return {"status": "ok"}
