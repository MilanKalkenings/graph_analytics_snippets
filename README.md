# Graph Analytics
### when to favor graph data representation?


dimension | relational database | graph data
|---|---|---|
entity-centric vs context-centric |focus on individual entities (rows) and their attributes (columns) in tables|entities (vertices) gain latent attributes from paths and neighborhoods formed by their relations (edges); supports dense interconnection
optimal relationship cardinality|one-to-many (one customer, multiple orders)|many-to-many (each user has many friends, each of the friends has many friends as well)
analysis focus | attribute aggregations (number of orders per customer) | edge existance, clusters, communities, neighborhoods, centrality
set-based vs path-based relations| set logic to connect tables with keys: left join: $L \cup (L \cap R)$, join: $L \cup R$|traverse graph along paths
recursive relations (A is manager of B, B is manager of C)|requires complex inefficient repeated joins |natively and efficiently supported
static vs dynamic schema|changing attribute and relation categories demands changing the whole data schema|attribute and relation categories can be added or removed dynamically
storage|efficiently stores entities and their attributes|efficiently stores entities, their attributes and their (dense) relations


### Examples for relations
- duration / evolution (until virus spreads, until next component is built, until customer upgrades subscription)
- cost (of transporting goods from location to location, to perform next task)
- similarity / difference (between names, between shapes, between number of customers in enterprise branches)
- interactions (between people or companies)
- references (citations, links)


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
  - graph: social network; edge: friendship
  - graph: knowledge graph; edge: relationship between entities/concepts 
- implemented methods: graph convolutional neural network

![link_prediction](https://github.com/user-attachments/assets/e7d0de56-d547-431c-a773-40770f6c3f38)


# Node Classification
- task: predict node level label for each node in a graph
- examples:
    - nodes: users, edges: user interactions , labels: troll y/n
    - nodes: documents, edges: doc similarity, labels: fake y/n
 
![node_classification_small](https://github.com/user-attachments/assets/fd304fc5-372a-4cef-80e5-634fd7650cb2)


