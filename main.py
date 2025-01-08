from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import numpy as np
from groq import Groq

app = FastAPI()

api_key = "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"

file_path = "bnsdataset.xlsx"
dataset = pd.read_excel(file_path)

required_columns = ['Section_Number','Subsection_Number', 'Title', 'Content', 'Explanation', 'Exception', 'Illustrations', 'Punishment','Cross_References']
if not all(column in dataset.columns for column in required_columns):
    raise ValueError(f"Dataset must contain the following columns: {required_columns}")

model = SentenceTransformer('all-MiniLM-L12-v2')

explanations = dataset['Explanation'].astype(str).tolist()
explanation_embeddings = model.encode(explanations)

class QueryRequest(BaseModel):
    query: str

def convert_numpy(obj):
    """Convert numpy objects to native Python types."""
    if isinstance(obj, (np.integer, np.floating)):
        return obj.item()
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    return obj

client = Groq(api_key=api_key)

def generate_human_like_response(section_data):
    """Generate a human-like response using the Groq API."""
    prompt = (
        f"Based on the following legal information, create a paragraph explanation for an Indian audience. Start with 'According to the Bharatiya Nyaya Sanhita (BNS),'. No mention of word India.:\n\n"
        f"Title: {section_data['Title']}\n"
        f"Content: {section_data['Content']}\n"
        f"Explanation: {section_data['Explanation']}\n"
        f"Exception: {section_data.get('Exception', 'No exceptions mentioned')}\n"
        f"Illustrations: {section_data['Illustrations']}\n"
        f"Punishment: {section_data['Punishment']}\n\n"
        "Please provide a detailed, human-like explanation and reformat the illustrations into a cohesive paragraph."
    )

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None
        )

        response_text = ""
        for chunk in completion:
            response_text += chunk.choices[0].delta.content or ""
        
        return response_text.strip()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Groq API error: {str(e)}")

@app.post("/get_legal_advice/")
async def get_legal_advice(request: QueryRequest):
    try:
        query_embedding = model.encode(request.query)
        similarities = util.cos_sim(query_embedding, explanation_embeddings)[0].tolist()
        best_match_idx = similarities.index(max(similarities))
        matched_row = dataset.iloc[best_match_idx]
        
        human_like_response = generate_human_like_response({
            "Title": matched_row['Title'],
            "Content": matched_row['Content'],
            "Explanation": matched_row['Explanation'],
            "Illustrations": matched_row['Illustrations'],
            "Punishment": matched_row['Punishment']
        })
        
        response_message = {
            "Category": "Criminal Law",
            "Section Number": convert_numpy(matched_row['Section_Number']),
            "Subsection Number": convert_numpy(matched_row['Subsection_Number']),
            "Cross References": matched_row['Cross_References'],
            "Punishment": matched_row['Punishment'],
            "Explanation": human_like_response
        }
        return response_message
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")