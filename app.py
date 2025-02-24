from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re
import requests
from generate_podcast import generate_podcast
from txtsum import generate_podcast_text
from cloudfuncs import export_to_cloud
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# WhatsApp API configuration
WHATSAPP_API_URL = "https://graph.facebook.com/v17.0/YOUR_PHONE_NUMBER_ID/messages"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"


# Define the structure of the incoming message
class IncomingMessage(BaseModel):
    from_number: str
    body: str


# Function to validate the message format (first name, last name, work email)
def validate_message(message: str) -> bool:
    return True
    # pattern = r"^[A-Za-z]+ [A-Za-z]+, [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    # return bool(re.match(pattern, message))


# Dummy podcast generation function (Replace with actual logic)
def generate_podcast_output(message: str) -> str:
    return generate_podcast(message)


# Function to send a WhatsApp message (API)
def send_whatsapp_message(to: str, message: str):
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message},
    }
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}
    response = requests.post(WHATSAPP_API_URL, json=payload, headers=headers)
    return response.json()


# Endpoint to handle incoming WhatsApp messages
@app.post("/webhook/")
async def handle_message(message: IncomingMessage):
    if validate_message(message.body):
        with open("data/three.txt", "r", encoding="utf-8") as file:
            message_content = file.read()
        podcast_audio = generate_podcast_output(message = message_content)
        text_doc = generate_podcast_text(message = message_content)
        external_audio = export_to_cloud(podcast_audio, bucket_name=os.getenv("GCS_BUCKET_NAME"), destination_blob_name="podcast.mp3")
        external_text = export_to_cloud(text_doc, bucket_name=os.getenv("GCS_BUCKET_NAME"), destination_blob_name="text_doc.txt")
        response_message = f"Your podcast is ready! Listen to it here: {external_audio} and check the document here: {external_text}"
        send_whatsapp_message(message.from_number, response_message)
        return {"status": "success", "message": response_message}
    else:
        raise HTTPException(status_code=400, detail="Invalid message format")


# For local testing (you can use uvicorn to run it)
# uvicorn app:app --reload
