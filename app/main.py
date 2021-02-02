import base64
import binascii
from typing import Optional
import fasttext

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

path_fasttext_model = "/model/lid.176.bin"

class Document(BaseModel):
    content: str

class Detector:
    def __init__(self, path_fasttext_model):
        self.fasttext_model = fasttext.load_model(path_fasttext_model)
    def fasttext_detect(self, text):
        text = " ".join(text.split())
        prediction = self.fasttext_model.predict([text])
        label = prediction[0][0][0]
        lang_code = label.replace('__label__', '')
        return lang_code

app = FastAPI()
detector = Detector(path_fasttext_model)

@app.post("/language-id")
async def get_language_id(document: Document):
    try:
        decoded_content = base64.b64decode(document.content).decode('utf-8')
    except binascii.Error:
        raise HTTPException(status_code=400, detail="Could not decode the 'content' field. Make sure it is in valid base64 encoding.")
    
    language_id = detector.fasttext_detect(decoded_content)

    output_json = {}
    output_json['language-id'] = language_id

    return output_json

    
