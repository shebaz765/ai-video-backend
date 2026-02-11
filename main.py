import os
import replicate
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
def generate_video(prompt: str):

    replicate_token = os.environ.get("REPLICATE_API_TOKEN")

    if not replicate_token:
        return {"error": "Replicate API token not found"}

    client = replicate.Client(api_token=replicate_token)

    output = client.run(
        "stability-ai/stable-video-diffusion",
        input={
            "prompt": prompt
        }
    )

    return {
        "status": "completed",
        "video_url": output
    }
