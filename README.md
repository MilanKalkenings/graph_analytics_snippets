# Graph Analytics
### when to favor graph data representation?


dimension | relational database | graph data
|---|---|---|
entity-centric vs context-centric |focus on individual entities (rows) and their attributes (columns) in tables|entities (vertices) gain latent attributes from paths and neighborhoods formed by their relations (edges); supports dense interconnection
optimal relationship cardinality|one-to-many (one customer, multiple orders)|many-to-many (each user has many friends, each of the friends has many friends as well)
analysis focus | attribute aggregations (number of orders per customer) | edge existance, clusters, communities, neighborhoods, centrality
set-based vs path-based relations| set logic to connect tables with keys: left join: $L \cup (L \cap R)$, join: $L \cup R$|traverse graph along paths
recursive relations (A is manager of B, B is manager of C)|requires complex inefficient repeated joins |natively and efficiently supported
storage|efficiently stores entities and their attributes|efficiently stores entities, their attributes and their (dense) relations


### Examples for relations
- weighted: cost / duration / similarity (time until next component is built / time until contrat ends / cost to perform next task / difference in number of customers / name similarity)
- binary: "has a contract with" / "cites" / "is synonyme of"


# Graph Classification
- task: predict graph-level label
- examples:
  - input: molecular structure; label: induces mutation in a bacterial strain y/n (implemented in my code using graph convolution and graph attention NN)
  - input: query, knowledge graph; label: graph contains information relevant for the query y/n (requires aligning query embedding and graph embedding)

![g_c](https://github.com/user-attachments/assets/4220ff13-abdc-4f67-9c51-a2e56f45d6eb)


# Link Prediction
- task: predict if edge exists (binary classification)
- examples:
  - nodes: tweets, edges: "refers to the same event" 
- implemented methods: graph convolutional neural network

![link_prediction](https://github.com/user-attachments/assets/e7d0de56-d547-431c-a773-40770f6c3f38)


# Node Classification
- task: predict node level label for each node in a graph
- examples:
    - nodes: users, edges: user interactions , labels: troll y/n
 
![node_classification_small](https://github.com/user-attachments/assets/fd304fc5-372a-4cef-80e5-634fd7650cb2)


