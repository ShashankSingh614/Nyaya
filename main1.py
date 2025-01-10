from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import numpy as np

app = FastAPI()

file_path = "bnsdataset.xlsx"
dataset = pd.read_excel(file_path)

# Handling NaN values in the dataset
dataset = dataset.fillna('No data available')  # Replace NaN with a placeholder

required_columns = ['Section_Number', 'Subsection_Number', 'Title', 'Content', 'Punishment', 'Cross_References']
if not all(column in dataset.columns for column in required_columns):
    raise ValueError(f"Dataset must contain the following columns: {required_columns}")

model = SentenceTransformer('all-MiniLM-L12-v2')

# Encode the content column for similarity matching
contents = dataset['Content'].astype(str).tolist()
content_embeddings = model.encode(contents)

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
        print("The model is currently in the testing phase. Please be advised that some NaN (Not a Number) values may appear. These values are being handled as part of the ongoing validation process. We are working diligently to ensure the accuracy and reliability of the model, and appreciate your understanding during this phase.")

        # Encode the user query
        query_embedding = model.encode(request.query)

        # Calculate cosine similarities
        similarities = util.cos_sim(query_embedding, content_embeddings)[0].tolist()
        best_match_idx = similarities.index(max(similarities))
        matched_row = dataset.iloc[best_match_idx]

        # Prepare the response
        response_message = {
            "Category": "Criminal Law",
            "Section Number": convert_numpy(matched_row['Section_Number']),
            "Subsection Number": convert_numpy(matched_row['Subsection_Number']),
            "Title": matched_row['Title'],
            "Content": matched_row['Content'],
            "Punishment": matched_row['Punishment'],
            "Cross References": matched_row['Cross_References']
        }
        return response_message
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
