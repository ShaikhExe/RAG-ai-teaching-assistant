import requests
import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_embedding(text_list):
    all_embeddings = []
    batch_size = 64

    for i in range(0, len(text_list), batch_size):
        batch = text_list[i:i + batch_size]

        r = requests.post(
            "http://localhost:11434/api/embed",
            json={
                "model": "bge-m3",
                "input": batch
            },
            timeout=300
        )

        if not r.ok:
            print("Batch failed:", i, r.status_code, r.text)
            r.raise_for_status()

        embeddings = r.json()["embeddings"]
        all_embeddings.extend(embeddings)

        print(f"Embedded {min(i + len(batch), len(text_list))}/{len(text_list)} chunks")

    return all_embeddings


jsons = os.listdir("jsons") # list all the jsons
my_dicts = []
chunk_id = 0

for json_file in jsons:

    with open(f"jsons/{json_file}") as f:
        content = json.load(f)
    print(f"Creating Embedding for {json_file}")
    
    embeddings = create_embedding([c['text'] for c in content['chunks']])

    for i, chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id+=1
        my_dicts.append(chunk)
        
df = pd.DataFrame.from_records(my_dicts)
# Save this dataframe
joblib.dump(df, 'embeddings.joblib')