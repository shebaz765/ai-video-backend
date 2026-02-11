import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

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
    return {"message": "AI Image Generator Running 🚀"}

@app.get("/generate")
def generate_image(prompt: str):

    image_url = f"https://image.pollinations.ai/prompt/{prompt}"

    response = requests.get(image_url)

    return Response(
        content=response.content,
        media_type="image/jpeg"
    )
