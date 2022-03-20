# helper functions
import torch
import pandas as pd
from sentence_transformers import SentenceTransformer, util

dataset = pd.read_csv("./data/dataset.csv")

# load a sentence-transformer model
model = SentenceTransformer('paraphrase-distilroberta-base-v1')

# encode queries from knowledge base to create corpus embeddings
corpus_embeddings = model.encode(dataset['Query'].tolist(), convert_to_tensor=True)

# lets put it all together
def get_query_responses(query, top_k=3):
    '''find the closest `top_k` queries of the corpus for the user query based on cosine similarity'''
    
    # encode user query
    query_embedding = model.encode(query, convert_to_tensor=True)

    # use cosine-similarity and torch.topk to find the highest `top_k` scores
    cos_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
    top_results = torch.topk(cos_scores, k=min(top_k, dataset.shape[0]))
    
    # filter dataframe by list of index
    df = dataset.iloc[top_results[1], :]
    
    # add matched score
    df['Score'] = ["{:.4f}".format(value) for value in top_results[0]]
    
    # select top_k responses
    responses = df.to_dict('records')
    
    return responses