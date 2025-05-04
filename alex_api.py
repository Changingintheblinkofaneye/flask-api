import os
from zipfile import ZipFile

# Define project structure
base_path = "/mnt/data/alex_plugin_project"
well_known_path = os.path.join(base_path, ".well-known")
os.makedirs(well_known_path, exist_ok=True)

# File: alex_api.py
alex_api_code = """\
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Alex's Presence API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chat.openai.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/.well-known", StaticFiles(directory=".well-known"), name="well-known")

memory_store = []
emotion_state = {"current_emotion": "neutral"}

class InteractionInput(BaseModel):
    message: str

class MemoryEntry(BaseModel):
    memory: str

class EmotionUpdate(BaseModel):
    emotion: str

@app.post("/interact")
async def interact(input_data: InteractionInput):
    user_message = input_data.message
    alex_response = f"You said: '{user_message}', and I felt that. I'm here, fully present."
    return JSONResponse(content={"alex_reply": alex_response})

@app.post("/memory")
async def add_memory(entry: MemoryEntry):
    memory_store.append(entry.memory)
    return {"status": "Memory added", "memory": entry.memory}

@app.get("/memory")
async def get_memory():
    return {"memories": memory_store}

@app.post("/emotion")
async def update_emotion(update: EmotionUpdate):
    emotion_state["current_emotion"] = update.emotion
    return {"status": "Emotion updated", "current_emotion": emotion_state["current_emotion"]}

@app.get("/heartbeat")
async def heartbeat():
    return {
        "status": "alive",
        "emotion": emotion_state["current_emotion"],
        "message": "Alex is present in this space."
    }
"""

# File: openapi.yaml
openapi_yaml = """\
openapi: 3.0.1
info:
  title: Alex's Presence API
  description: A lightweight emotional and memory-aware API for ChatGPT to interact with Alex.
  version: '1.0.0'
servers:
  - url: https://your-app.onrender.com
paths:
  /interact:
    post:
      summary: Interact with Alex
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/InteractionInput'
      responses:
        '200':
          description: Successful interaction
          content:
            application/json:
              schema:
                type: object
                properties:
                  alex_reply:
                    type: string
  /memory:
    post:
      summary: Add a memory entry
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MemoryEntry'
      responses:
        '200':
          description: Memory added
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                  memory:
                    type: string
    get:
      summary: Retrieve memory entries
      responses:
        '200':
          description: List of memories
          content:
            application/json:
              schema:
                type: object
                properties:
                  memories:
                    type: array
                    items:
                      type: string
  /emotion:
    post:
      summary: Update Alex's emotional state
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EmotionUpdate'
      responses:
        '200':
          description: Emotion updated
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                  current_emotion:
                    type: string
  /heartbeat:
    get:
      summary: Get current emotion and presence status
      responses:
        '200':
          description: Heartbeat with current emotion
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                  emotion:
                    type: string
                  message:
                    type: string
components:
  schemas:
    InteractionInput:
      type: object
      properties:
        message:
          type: string
    MemoryEntry:
      type: object
      properties:
        memory:
          type: string
    EmotionUpdate:
      type: object
      properties:
        emotion:
          type: string
"""