# Local LLM Setup

This repository contains scripts and examples for running a large
language model locally and exposing it as a simple HTTP API. Running
models on your own hardware helps you maintain control of your data
and avoid recurring API costs.

## Requirements

* A modern computer with **16 GB of RAM or more** and preferably a GPU
  (models will run on the CPU but performance improves with a GPU)【981496197263263†L104-L123】.
* Python 3.8+ installed on the system.
* (Optional) A virtual environment to isolate Python dependencies.

## Files

* `setup.sh` – Shell script that creates a Python virtual
  environment, installs the `gpt4all` and `flask` packages, and triggers
  the download of a light‑weight Mistral model. After running this
  script you will have a ready‑to‑use environment for local inference.
* `local_llm_server.py` – A minimal Flask server that loads a model via
  GPT4All and exposes a `/chat` endpoint. Post a JSON payload like
  `{ "prompt": "Hello" }` to receive a generated response.

## Setup

```bash
git clone https://github.com/mentiminder/local-llm-setup.git
cd local-llm-setup

# Make the setup script executable and run it
chmod +x setup.sh
./setup.sh

# Activate the virtual environment and start the server
source venv/bin/activate
python local_llm_server.py

# In a separate terminal, send a request using curl:
curl -X POST -H "Content-Type: application/json" \
  -d '{"prompt": "Tell me a fun fact about dolphins"}' \
  http://localhost:8000/chat
```

The first time you run the server it will download the specified
model. You can change the model by editing the `MODEL_NAME` variable
in `local_llm_server.py` or by setting the `GPT4ALL_MODEL`
environment variable before starting the server.

## Choosing a model

GPT4All provides numerous models with varying sizes and capabilities. A
light‑weight model like `mistral-7b-instruct-v0.1.q4_0` will run on most
modern PCs. You can explore additional models via the GPT4All
documentation or use other local LLM tools such as LM Studio (which
supports models like Qwen, Gemma and DeepSeek)【969977271736245†L20-L24】
or Jan.ai (an open‑source ChatGPT alternative that runs 100 % offline)【257377221026874†L21-L62】.

## Important notes

* Running large language models locally can be resource intensive. If
  your computer struggles with the default model, switch to a smaller
  model in GPT4All.
* This repository is a starting point; you can extend the API server
  with authentication, logging, or additional endpoints to suit your
  use cases.