import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Image to Video Backend Running 🚀"}

@app.get("/generate")
def generate(prompt: str):
    
    # 5 free images from Unsplash
    images = [
        "https://source.unsplash.com/800x600/?nature",
        "https://source.unsplash.com/800x600/?city",
        "https://source.unsplash.com/800x600/?technology",
        "https://source.unsplash.com/800x600/?night",
        "https://source.unsplash.com/800x600/?space"
    ]

    return {
        "status": "completed",
        "images": images
    }
