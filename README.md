# Graph Classification
- task: predict graph-level label
- examples:
  - input: street network; label: efficient y/n
  - input: molecular structure; label: induces mutation in a bacterial strain y/n (implemented in my code)
  - input: query, knowledge graph; label: the graph fulfills properties stated in the query y/n (needs allignment of query embedding and graph embedding)
  - input: online community; label: community structure type
- implemented methods: graph convolutional neural network, graph attention neural network

![g_c](https://github.com/user-attachments/assets/4220ff13-abdc-4f67-9c51-a2e56f45d6eb)


# Link Prediction
- task: predict if edge exists (binary classification)
- examples:
  - graph: social network; edge: people are friends with each other
  - graph: knowledge graph; edge: relationship between entities/concepts 
- implemented methods: graph convolutional neural network

![link_prediction](https://github.com/user-attachments/assets/5471b19e-7b54-46b7-83c0-1d251a22fd9e)
