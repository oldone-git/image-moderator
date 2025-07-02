from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import requests
import os
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()
DEEPAI_API_KEY = os.getenv("DEEPAI_API_KEY")

@app.post("/moderate")
async def moderate_image(file: UploadFile = File(...)):
  
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return JSONResponse(
            status_code=400,
            content={"error": "Only .jpg and .png files are allowed"}
        )
    
   
    image_data = await file.read()
    
    
    response = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        files={'image': image_data},
        headers={'api-key': DEEPAI_API_KEY}
    )
    
  
    result = response.json()
    nsfw_score = result.get('output', {}).get('nsfw_score', 0)
    
    if nsfw_score > 0.7:
        return {"status": "REJECTED", "reason": "NSFW content"}
    return {"status": "OK"}
