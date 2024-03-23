# Generate ARM templates using RAG

## Introduction

The aim of this project is to understand if RAG can be used to generate meaningful IaC templates. I am using Azure and trying to generate ARM templates. [Ollama](https://ollama.com/) is used as run LLMs locally on my machine. [LlamaIndex](https://www.llamaindex.ai/) is the python framework used to build the RAG system. For data source I have used sample arm templates from [official Azure repository](https://github.com/Azure/azure-quickstart-templates). 

## Features

- **LLM Integration**: Seamlessly integrates with Ollama for accessing and managing state-of-the-art language models.
- **Framework Support**: Built on the llamaIndex framework, providing a robust set of tools for LLM application development.

## Getting Started

### Installation

1. **Clone the Repository**

```bash
git clone https://github.com/vishwajeetk1160/arm-template-generator.git
cd repository
```
2. **Prerequisites**
- Python 3.10 or higher
- Jupyter Notebook
- Ollama(mistral:7b, llama2:7b, gemma:2b)
- ```bash
  pip install requirements.txt
  ```
3. **Repository structure**
```
.
├── data
│   ├── armTemplate1.json
│   ├── armTemplate2.json
├── indexes
└── arm-template-helper.ipynb
```
- `indexes` folder will be populated when you create index for the data.
- `arm-template-helper.ipynb` is the python notebook which reads the data and creates index for it in indexes folder. It then queries the LLM to get answers. You can select from a set of LLMs depending on what is installed in your local machine using Ollama.
- [RAG basics](https://docs.llamaindex.ai/en/stable/getting_started/concepts/)