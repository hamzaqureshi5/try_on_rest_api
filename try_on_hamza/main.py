# import requests

# url = 'https://api.jina.ai/v1/embeddings'

# headers = {
#   'Content-Type': 'application/json',
#   'Authorization': 'Bearer jina_19d1fe674e6a494eb4339d0b404bb83bpfQ-RUo8zBdNECI0s3ZlWf1bf8Qb'
# }
# # "jina_19d1fe674e6a494eb4339d0b404bb83bpfQ-RUo8zBdNECI0s3ZlWf1bf8Qb"

# data = {
#   'input': ["I am hamza"],
#   'model': 'jina-embeddings-v2-base-en'
# }

# response = requests.post(url, headers=headers, json=data)

# print(response.json())
from langchain_community.embeddings import JinaEmbeddings
import numpy as np
KEY="jina_19d1fe674e6a494eb4339d0b404bb83bpfQ-RUo8zBdNECI0s3ZlWf1bf8Qb"
embeddings = JinaEmbeddings(jina_api_key = KEY, model_name="jina-embeddings-v2-base-en")
# text = "This is a test document."
text = "I like cat"
query_result = embeddings.embed_query(text)

# text1 = "This is a text document."
text1 = "I like cats"

query_result1 = embeddings.embed_query(text1)

print(len(query_result))

print(np.dot(query_result,query_result1))
# print(query_result)