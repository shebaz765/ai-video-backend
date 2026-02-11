import os
import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Image to Video Backend Running 🚀"}


@app.get("/generate")
def generate(prompt: str):

    # 5 free images from Unsplash based on prompt
    images = [
        f"https://source.unsplash.com/800x600/?{prompt},nature",
        f"https://source.unsplash.com/800x600/?{prompt},city",
        f"https://source.unsplash.com/800x600/?{prompt},technology",
        f"https://source.unsplash.com/800x600/?{prompt},night",
        f"https://source.unsplash.com/800x600/?{prompt},space"
    ]

    # Download images locally
    for i, url in enumerate(images):
        img_data = requests.get(url).content
        with open(f"image{i}.jpg", "wb") as handler:
            handler.write(img_data)

    # Create video using ffmpeg
    subprocess.run(
        "ffmpeg -y -r 1 -i image%d.jpg -c:v libx264 -vf fps=25 -pix_fmt yuv420p output.mp4",
        shell=True
    )

    return FileResponse("output.mp4", media_type="video/mp4", filename="video.mp4")
