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
