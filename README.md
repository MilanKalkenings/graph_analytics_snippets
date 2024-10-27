# Graph Analytical Thinking

Dimension | Relational Database | Graph Analytical
|---|---|---|
entity-centric vs context-centric |focus on individual entities (rows) and their attributes (columns) in tables|entities (vertices) gain latent attributes from paths and neighborhoods formed by their relations (edges); supports dense interconnection
one-to-many vs Mmany-to-many relations | attribute aggregations (number of orders per customer) | (common) connections, contexts, neighborhoods
set-based vs path-based relations| connect tables with keys using set logic: left join ($L \cup (L \cap R)$, all entities in left table and their attributes in right table), join ($L \cup R$, entities occuring in both tables)|traverse interconnected graph with Cycles (A is friend of B, B is friend of C, C is friend of A), Recursions (A is manager of B, B is manager of C)
static vs dynamic schema|types of attributes and relations are rigidly defined and adding new forms of them demands challenging schema modifications|types of attributes and relations can be added or removed dynamically
storage|efficiently stores entities and their attributes|efficiently stores entities, their attributes and their relations

## Examples for relations
- duration / evolution (until virus spreads, until next component is built, until customer upgrades subscription)
- cost (of transporting goods from location to location, to perform next task)
- similarity / difference (between names, between shapes, between number of customers in enterprise branches)


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

![link_prediction](https://github.com/user-attachments/assets/e7d0de56-d547-431c-a773-40770f6c3f38)


# Node Classification
- task: predict node level label for each node in a graph
- examples:
    - nodes: users, edges: user interactions , labels: troll y/n
    - nodes: documents, edges: doc similarity, labels: fake y/n
 
![node_classification_small](https://github.com/user-attachments/assets/fd304fc5-372a-4cef-80e5-634fd7650cb2)


