## Introduction

Welcome to **EvalMaster**, an advanced evaluation framework leveraging the power of the Llama-Index and Llama-CPP frameworks, along with the cutting-edge **Prometheus-2** model. This project aims to provide a robust and flexible evaluation tool for assessing the performance of language models using various evaluation metrics.

## Features

- **Pairwise Comparison Evaluation**: Compares two responses to determine the better one for a given query.
- **Correctness Evaluation**: Assesses the accuracy of a response against a reference answer.
- **Faithfulness Evaluation**: Evaluates if the response stays true to the input query without deviating.
- **Relevancy Evaluation**: Measures how relevant a response is to the given query.

## Project Overview

This project uses the Llama-Index framework to build an evaluator based on the Prometheus-2 model. The Prometheus-2 model is loaded using the Llama-CPP framework, specifically using the gguf quantized version of prometheus-7b-v2.0 model. The data is stored in a WeaviateVectorStore, allowing for efficient querying and retrieval.

## Query Engines

We evaluate two types of query engines for testing purposes:
- **Hybrid Query Engine**: Combines keyword search and similarity search for more comprehensive results.
- **Default Query Engine**: Uses only similarity search, with options for user customization.

These query engines are provided as examples; you can use any generated response from your Retrieval-Augmented Generation (RAG) system for evaluation.

## Evaluation Functions

The project demonstrates the use of Prometheus-2 with the following evaluators available in Llama-Index:

1. **Pairwise Evaluator**: Determines the preferred response between two given options.
2. **Faithfulness Evaluator**: Ensures the response is faithful to the retrieved contexts, minimizing hallucination.
3. **Correctness Evaluator**: Checks if the generated response matches a provided reference answer.
4. **Relevancy Evaluator**: Assesses the relevance of the response to the given query.

## Prometheus-2 Model

Prometheus-2 is designed as a powerful alternative to proprietary models like GPT-4 for fine-grained evaluation. It supports both direct assessment (absolute grading) and pairwise ranking (relative grading). Prometheus-2 is based on the Mistral-7B and Mixtral8x7B models, fine-tuned with extensive feedback data to closely mirror human and GPT-4 judgments.

## How to Use This

To use this project, follow these steps:

1. **Clone the repository and navigate to the project directory**:
   ```sh
   git clone https://github.com/your-username/EvalMaster.git
   cd EvalMaster
   ```

2. **Install the necessary dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Move your data files (pdf, csv, md, etc.) to the `src/data_input` folder**.

4. **Create a `.env` file with the following content**:
   ```
   WCD_DEMO_URL=.........
   WCD_DEMO_RO_KEY=........
   CO_API_KEY=..........
   ```

5. **Download the gguf model and move it to the `src/model_path` folder**:
   ```sh
   wget https://huggingface.co/vsevolodl/prometheus-7b-v2.0-GGUF/resolve/main/prometheus-7b-v2.0.Q8_0.gguf
   ```

6. **Run `main.py` by passing the query and reference**. The evaluation should start and it will take some time, especially when you are using a CPU instead of a GPU.
   ```sh
   python main.py "Your query here" "Your reference data here"
   ```

### Example

```sh
python main.py "What is the capital of France?" "The capital of France is Paris."
```
