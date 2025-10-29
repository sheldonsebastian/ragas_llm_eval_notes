# Exploring RAGAS for evaluating LLMs

![Disclaimer](https://img.shields.io/badge/Disclaimer-Human_created_images._Human_reviewed_AI_text_&_code-red?style=for-the-badge)

This repository contains my notes and experiments for evaluating LLMs using the RAGAS framework, compiled while following a **[Udemy course](https://www.udemy.com/certificate/UC-82acbab2-2ea4-46e4-8d6a-41a53062715a)**.

Use the map below to navigate the repository:
<image src="assets/Map to explore repo.png">

## Repository Hierarchy

| File | Purpose |
| ---- | ------- |
| `0_rag_setup.ipynb` | RAG overview and step‑by‑step local setup (environment, dependencies, and getting a working retrieval + generation pipeline). |
| `1_rag_metrics.ipynb` | Explanation of evaluation metrics used for RAG (definitions, examples, and reference implementations). |
| `2_generate_test_data.ipynb` | Procedures to generate and preprocess test datasets used for evaluations. |
| `3_eval_on_test_data.ipynb` | Runs RAG evaluations using the setup from `0_rag_setup.ipynb` and data from `2_generate_test_data.ipynb`; collects and summarizes metrics and outputs. |
|`helpers.py`| Helper functions used in `3_eval_on_test_data.ipynb`|

## Steps to run locally

1. Create the conda environment

    ```bash
    conda create --name ragas_llm_eval python=3.12 -y
    ```

2. Activate the environment

    ```bash
    conda activate ragas_llm_eval
    ```

3. Install Python dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Set the OpenAI API key
    - Create a `configs.env` file based on `configs.env_sample` and set:
        - `OPENAI_API_KEY=your_key_here`

    - Expected usage is low (~$10); monitor your API usage and quotas.

5. Run the notebooks in order
    - Open and run each notebook sequentially to reproduce results:
    - `0_rag_setup.ipynb`
    - `1_rag_metrics.ipynb`
    - `2_generate_test_data.ipynb`
    - `3_eval_on_test_data.ipynb`

6. Troubleshooting tips
    - If notebooks fail due to missing credentials, ensure `configs.env` is in the repo root and contains a valid `OPENAI_API_KEY`.

## Data Sources

The text files used in this project are sourced from **[Project Gutenberg](https://www.gutenberg.org/)** — a free online library of public domain works.

| Book Title                                    | Author                              | Project Gutenberg Link                                                         |
| --------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------ |
| *Dracula*                                     | Bram Stoker                         | [https://www.gutenberg.org/ebooks/345](https://www.gutenberg.org/ebooks/345)   |
| *The Adventures of Sherlock Holmes*           | Arthur Conan Doyle                  | [https://www.gutenberg.org/ebooks/1661](https://www.gutenberg.org/ebooks/1661) |

> **Note:** All texts are in the public domain and are made available by Project Gutenberg under their [Terms of Use](https://www.gutenberg.org/policy/license.html).
