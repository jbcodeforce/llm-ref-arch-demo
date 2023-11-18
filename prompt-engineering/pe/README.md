# Prompt engineering demo

This app demonstrates some prompt engineering effect. Prompt engineering is the practice of optimizing the quality and performance of your foundation model's response to your request. Prompt engineering may involve:

* Word choice
* Phrasing
* Providing examples (few-shot learning)

## Basic

Give context vias the input text:

```sh
What was the high temperature yesterday?
```

Should not get good result, while the following does:

```sh
The low temperature yesterday was 30 degrees Fahrenheit, and the high was 48 degrees.
What was the high temperature yesterday?
```


In order to maintain a conversation, we must "remind" the model about our conversation up until this point. This usually comes in the form of past messages, a summary of the conversation, or a combination of both.

```sh
What is the capital of New Hampshire?
The capital of New Hampshire is Concord.
What is the capital's population?
```

## Content creation

* Brainstorming

```sh
Please create a list of startup ideas for a new generative AI service for the food industry:
```

or

```sh
Please create a list of startup ideas for a new generative AI service for the food restaurants. The target 
market is french people living in america. For each startup idea, provide a name and a one-sentence elevator pitch for what the startup will do.
```

* outline 

```json
{context}

Write an outline for a blog article about the service described above:
```

```json
{context}

Write a marketing plan for the service described above:
```

* Draft Q&A

```json
{context}

Write a marketing plan for the service described above. Be sure to answer the following in the marketing plan:

Who is the person using the product?
What is the unmet need that will be satisified by the product?
Who is the buyer of the product?
What is the go-to-market strategy for the product?

```

* Rewrite content with constraints

```sh
{context}

Write a marketing brochure based on the above content. The marketing brochure should be targeted to an executive business audience. Avoid the use of technical jargon and acronyms.
```

* Rewrite from bullet points

```sh
Use cases for generative AI:
* Summarizing large documents
* Answering questions based on a body of knowledge
* Analyzing content and providing recommendations
* Creating new content

Please write an introductory paragraph to a blog article highlighting the above use cases:
```

* Generate FAQ:

```json
{context}

Write an FAQ based on the above content:
```