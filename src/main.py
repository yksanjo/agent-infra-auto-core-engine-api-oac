"""auto-core-engine-api-oac - AI Infrastructure Component"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"service": "auto-core-engine-api-oac", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
