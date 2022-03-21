# Improving Business Processes Using ML-Based Contact Form

Imagine your business has a contact form on its website. Every day you get many messages from the form, many of which are actionable, but it's easy to fall behind on dealing with them since different employees handle different queries. It would be great if an automated system could responds to the incoming queries that helps in assit the process and reduce levels of manual support.

## Solution

We will build an automated system that uses a [semantic similarity](https://arxiv.org/abs/1908.10084) model to match query from form to those in our knowledge base. Semantic similarity methods use a siamese (dual) transformers ML model to compare the numerical representation (embeddings) of two sentences. By calculating cosine similarity between the embeddings of queries in our knowledge base and the query the user asked, we can provide accurate answers to the user based on human-curated information.

Our system will funtions through the following process:

1. User asks their question through form
2. Model compares their question to the knowledge base to find the most closet entry
3. Model gives the answer associated with the most similar question from the knowledge base

## Knowledge Base

We can convert any FAQs into knowledge base. In this example, we will consider the below sample dataset:
| Query      | Response |
| ----------- | ----------- |
| I would like to pay online? | Thank you for connecting. You can pay by visiting http://abc.com/pay |
| Trying to setup new account | Thank you for connecting. You can apply for here: http://abc.com/apply.  If you need assistance, you can contact us at 1234567. |
| Please send outstanding bills for my service | Thank you for connecting. You will receive the outstanding bills on registered email address. |

## Implementation

We will use [`sentence_transformers`](https://www.sbert.net/) is a very popular approach deployed for semantic search, semantic similarity and clustering. You can read below code block with comments and output for more understanding:

```python
# import required libraries
import torch
import pandas as pd
from sentence_transformers import SentenceTransformer, util

# load the dataset(knowledge base)
dataset = pd.read_csv("../data/dataset.csv")

# load a sentence-transformer model
model = SentenceTransformer('paraphrase-distilroberta-base-v1')

# encode queries from knowledge base to create corpus embeddings
corpus_embeddings = model.encode(dataset['Query'].tolist(), convert_to_tensor=True)

# user query
query = "I want to pay my bill"

# find the closest `top_k` queries of the corpus for the user query based on cosine similarity
top_k = 1

# encode user query
query_embedding = model.encode(query, convert_to_tensor=True)

# use cosine-similarity and torch.topk to find the highest `top_k` scores
cos_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
# output: tensor([0.5136, 0.3416, 0.2005, 0.0468, 0.3057, 0.5580, 0.3149, 0.7042, 0.1120])

top_results = torch.topk(cos_scores, k=min(top_k, dataset.shape[0]))
# output: torch.return_types.topk(values=tensor([0.7042,]), indices=tensor([7,]))

# filter dataframe by list of index
df = dataset.iloc[top_results[1], :]

# add matched score
df['Score'] = ["{:.4f}".format(value) for value in top_results[0]]

# convert the result to dict
df.to_dict('records')
# output: [{'Query': 'How can I pay my bill?',
#           'Response': 'Thank you for connecting. You can pay by visiting http://abc.com/pay',
#           'Score': '0.7042'}
#         ]
```

## Let's put it all together

To put it all together, I have developed an interactive app using [Streamlit](https://streamlit.io/). I would recommend checking out the link [here](https://github.com/imnileshd/nlp-sentence-transformer) that covers the entire code and the requirements that are necessary to successfully deploy this app.

## Deploy an app

Now that we have created our data app, and ready to share it! We can use [Streamlit Cloud](https://streamlit.io/cloud) to deploy and share our app. Streamlit Cloud has multiple tiers, the free Community tier is the perfect solution if your app is hosted in a public GitHub repo and you'd like anyone in the world to be able to access it.

You can check steps to deploy apps with the free Community tier [here](https://docs.streamlit.io/en/stable/deploy_streamlit_app.html).

Now my app is live and you can interact with it [here](https://share.streamlit.io/imnileshd/nlp-sentence-transformer).

## Conclusion

Thank you for reading! I hope this article was valuable to you and you enjoyed the walkthrough.

By using this approach, we can set up effective systems quickly to save time for business process use cases that generally require human intervention.

Happy Coding!
