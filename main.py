import os
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from moviepy.editor import ImageClip

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
    return {"message": "AI Image to Video Generator Running 🚀"}


@app.get("/generate")
def generate_video(prompt: str):

    # Free AI image generation (Pollinations)
    image_url = f"https://image.pollinations.ai/prompt/{prompt}"

    image_path = "image.jpg"
    video_path = "output.mp4"

    # Download image
    response = requests.get(image_url)
    with open(image_path, "wb") as f:
        f.write(response.content)

    # Convert image to 5-second video
    clip = ImageClip(image_path).set_duration(5)
    clip.write_videofile(video_path, fps=24)

    return FileResponse(video_path, media_type="video/mp4", filename="ai_video.mp4")
