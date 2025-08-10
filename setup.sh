#!/bin/bash

# Script to set up a Python virtual environment and install
# dependencies for running a local large language model using
# the GPT4All library. It also downloads a small model and
# prepares the system to start a simple API server.

set -e

echo "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing required Python packages..."
# gpt4all provides bindings to download and run models locally. Flask
# will be used to expose a simple HTTP API for the model.
pip install gpt4all==1.3.0 flask==3.0.2

echo "Downloading a default model (this may take a while)..."
# The GPT4All package will automatically download the specified
# model on first use. Here we run a small Python snippet to trigger
# the download of a light‑weight Mistral model. You can change the
# model name to any supported model; see the GPT4All documentation
# for available options.
python3 - <<'PY'
from gpt4all import GPT4All

model_name = "mistral-7b-instruct-v0.1.q4_0"
print(f"Downloading model {model_name} if not already present...")
_ = GPT4All(model_name)
print("Model download complete.")
PY

echo "Setup complete. To start the API server, run:"
echo "source venv/bin/activate && python local_llm_server.py"