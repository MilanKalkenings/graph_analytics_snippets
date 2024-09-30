# Graph Classification
- task: predict graph-level label
- examples:
  - input: street network; label: efficient y/n
  - input: molecular structure; label: induces mutation in a bacterial strain y/n (implemented in my code)
  - input: query, knowledge graph; label: the graph fulfills properties stated in the query y/n (needs allignment of query embedding and graph embedding)
  - input: online community; label: community structure type
- implemented methods: graph convolutional neural network, graph attention neural network
