# Image Moderator

FastAPI application for image moderation using DeepAI NSFW detector.

## Features
- Image upload endpoint
- Integration with DeepAI NSFW detector
- Support for JPG and PNG formats
- Simple JSON response format

## Setup

1. Clone the repository
```bash
git clone https://github.com/oldone-git/image-moderator
cd image-moderator

    Create virtual environment

python -m venv venv
venv\Scripts\activate  # Windows

    Install dependencies

pip install -r requirements.txt

    Create .env file with your DeepAI API key

DEEPAI_API_KEY=your_api_key_here

    Run the server

uvicorn app.main:app --reload

API Endpoints
POST /moderate

Upload image for moderation.
Request

    Method: POST
    Endpoint: /moderate
    Content-Type: multipart/form-data
    Body: file (image/jpeg or image/png)

Response

Success (200 OK):

{
    "status": "OK"
}

NSFW Content Detected:

{
    "status": "REJECTED",
    "reason": "NSFW content"
}

Usage Examples
Using curl

curl -F "file=@path/to/image.jpg" http://localhost:8000/moderate

Using Python requests

import requests

files = {'file': open('image.jpg', 'rb')}
response = requests.post('http://localhost:8000/moderate', files=files)
print(response.text)

Using Swagger UI

    Open http://localhost:8000/docs in your browser
    Navigate to POST /moderate endpoint
    Click "Try it out"
    Upload an image file
    Click "Execute"

Technical Details

    Python 3.13
    FastAPI 0.115.14
    Uses DeepAI's NSFW detector API
    NSFW threshold set to 0.7

Requirements

See requirements.txt for full list of dependencies.
