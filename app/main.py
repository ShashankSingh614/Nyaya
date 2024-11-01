from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq

# Initialize the Groq client with your API key
client = Groq(api_key="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")

app = FastAPI()

# Predefined examples for context
examples = [
    {"role": "user", "content": "Please provide legal advice based on Indian Penal Code (IPC) sections and explain why each section is applicable."},
    {"role": "assistant", "content": 
        "Here are a few IPC sections for reference:\n"
        "- IPC 131: Abetting mutiny, or attempting to seduce an officer, soldier sailor, or airman from his allegiance. Punishment: Imprisonment for Life or 10 Years + Fine.\n"
        "- IPC 132: Abetment of mutiny if mutiny is committed. Punishment: Death or Imprisonment for Life or 10 Years + Fine.\n"
        "..."
    }, 
]

# Define request body model
class QueryRequest(BaseModel):
    query: str

@app.post("/get_legal_advice/")
async def get_legal_advice(request: QueryRequest):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=examples + [{"role": "user", "content": request.query}],
            temperature=0.8,
            max_tokens=500,
            top_p=1,
            stop=None,
        )
        response_content = completion.choices[0].message.content
        return {"response": response_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))