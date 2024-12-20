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

# Multi-Agent Pathfinding 
- agents have to reach goals in minimal time without colliding with obstacles or other agents
- Each goal is locked on by agent with shortest path to the goal (Breadth First Search)
- Collisions between agents are prevented while minimizing swarm travel costs (Hungarian Algorithm Movement Assignment)

![swarm](https://github.com/user-attachments/assets/b7b82e22-2657-4c89-85a2-9097985b2349)



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


# Centrality
- measures how "central" / "connected" / "influential" a node is
- implemented for node classification

![graph_centrality](https://github.com/user-attachments/assets/c30cbd7c-ea4a-4dd0-abbc-25b6ebe0976c)

<img width="770" alt="table_centrality" src="https://github.com/user-attachments/assets/46424bac-3487-4812-b940-8251c1700d91">

centrality measure correlation on [youtube communities](https://snap.stanford.edu/data/com-Youtube.html):

<img width="127" alt="centrality_corr_youtube" src="https://github.com/user-attachments/assets/0606322b-d580-478b-a849-815b06598de8">



