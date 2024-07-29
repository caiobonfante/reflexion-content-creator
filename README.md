# Reflexion Agent for Social Media Post Creation

This project implements a Reflexion Agent using LangGraph and LangChain to create optimized posts for social media, with an initial focus on LinkedIn. The agent leverages external references and iterative self-reflection to generate accurate and contextually relevant content, significantly reducing the risk of hallucinations commonly associated with large language models.

Entendi. Vou atualizar o README para refletir o uso do Poetry como gerenciador de dependências do projeto. Aqui está a versão revisada das seções relevantes em inglês:

## Prerequisites

Make sure you have installed:

- Python 3.8+
- Poetry (dependency management tool)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

3. Set up environment variables in a .env file:
   ```
   OPENAI_API_KEY=your_api_key_here
   TAVILY_API_KEY=your_api_key_here
   ```


## Usage

To run the agent:

```
poetry run python main.py
```

## Main Dependencies

All dependencies are managed through Poetry. The main ones include:

- Python
- OpenAI
- Tavily
- LangGraph
- LangChain

You can view all dependencies in the `pyproject.toml` file.