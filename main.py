from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import numpy as np

app = FastAPI()

file_path = "E:/Shashank Singh/Coding/Nyaya using Llama/dataset/bnsdataset.xlsx"
dataset = pd.read_excel(file_path)

required_columns = ['Section_Number', 'Title', 'Content', 'Explanation', 'Illustrations', 'Punishment']
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

@app.post("/get_legal_advice/")
async def get_legal_advice(request: QueryRequest):
    try:
        query_embedding = model.encode(request.query)
        similarities = util.cos_sim(query_embedding, explanation_embeddings)[0].tolist()
        best_match_idx = similarities.index(max(similarities))
        matched_row = dataset.iloc[best_match_idx]
        response_message = {
            "Section_Number": convert_numpy(matched_row['Section_Number']),
            "Title": matched_row['Title'],
            "Content": matched_row['Content'],
            "Punishment": matched_row['Punishment'],
            "Explanation": matched_row['Explanation'],
            "Illustrations": matched_row['Illustrations']
        }
        return response_message
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
