from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Video Generator Backend Running 🚀"}

@app.get("/generate")
def generate_video(prompt: str, duration: int):
    return {
        "status": "processing",
        "prompt": prompt,
        "duration": duration,
        "message": "Video generation started"
    }
