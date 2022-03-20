# Improving Business Processes Using Smart Contact Form

Imagine your business has a contact form on its website. Every day you get many messages from the form, many of which are actionable, but it's easy to fall behind on dealing with them since different employees handle different queries. It would be great if an automated system could responds to the incoming queries that helps in assit the process and reduce levels of manual support.

## Solution

We will build an automated system that uses a [semantic similarity](https://arxiv.org/abs/1908.10084) model to match query from form to those in our knowledge base. Semantic similarity methods use a siamese (dual) transformers ML model to compare the numerical representation (embeddings) of two sentences. By calculating cosine similarity between the embeddings of queries in our knowledge base and the query the user asked, we can provide accurate answers to the user based on human-curated information.

Our system will funtions through the following process:

1. User asks their question through form
2. Model compares their question to the knowledge base to find the most closet entry
3. Model gives the answer associated with the most similar question from the knowledge base

<!-- Image -->

## Knowledge Base

## Implementation

## Let's put it all together

To put it all together, I have developed an interactive app using [Streamlit](https://streamlit.io/). I would recommend checking out the link [here](https://github.com/imnileshd/nlp-sentiment-analysis) that covers the entire code and the requirements that are necessary to successfully deploy this app.

## Deploy an app

Now that we have created our data app, and ready to share it! We can use [Streamlit Cloud](https://streamlit.io/cloud) to deploy and share our app. Streamlit Cloud has multiple tiers, the free Community tier is the perfect solution if your app is hosted in a public GitHub repo and you'd like anyone in the world to be able to access it.

You can check steps to deploy apps with the free Community tier [here](https://docs.streamlit.io/en/stable/deploy_streamlit_app.html).

Now my app is live and you can interact with it [here](https://share.streamlit.io/imnileshd/nlp-sentiment-analysis).

## Conclusion

Thank you for reading! I hope that this project walkthrough inspires you to create your own sentiment analysis model.

Happy Coding!
