# A Reference Architecture for LLM solution in EDA world

A generic reference architecture for a LLM solution looks like in the following diagram:

![](./docs/diagrams/llm-ra-1.drawio.png)

1. **Data pipelines** are batch processing, which in the context of LLM may mix processing of unstructured documents with structured CSVs, Json, or SQL tables. data done in map-reduce platform to do Extract Transform Load job. Most of existing pipelines land their output to Data Lake. But modern pipeline may call directly a LLM to build embeddings to be saved into Vector Store. The flow will look like in the figure below, which is based on classical Retrieval augmented generation (RAG) process.

    ![](./docs/diagrams/rag-process.drawio.png)

1. **Streaming** is where connection to event-driven architecture land: a lot of business services / microservices are generating important events to be part of the future context of the end user interaction with the application. Those events can be aggregated, and a similar pipeline can be done with streaming application, consuming events, and doing the embedding via LLM calls then push to Vector Store.
1. **Embeddings** open-source, the [Sentence Transformers library from Hugging Face](https://huggingface.co/sentence-transformers)