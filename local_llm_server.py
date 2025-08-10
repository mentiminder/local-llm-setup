"""
Simple HTTP API server for interacting with a locally hosted large
language model using GPT4All. The server exposes a single `/chat`
endpoint that accepts a JSON payload with a "prompt" field and
returns a generated response.

Usage:
    source venv/bin/activate
    python local_llm_server.py

The server listens on port 8000 by default. You can change the port
by setting the `PORT` environment variable.
"""

import os
from flask import Flask, request, jsonify
from gpt4all import GPT4All


MODEL_NAME = os.environ.get("GPT4ALL_MODEL", "mistral-7b-instruct-v0.1.q4_0")

app = Flask(__name__)

print(f"Loading model {MODEL_NAME}... This may take a few moments on first run.")
model = GPT4All(MODEL_NAME)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    prompt = data.get("prompt", "").strip()
    if not prompt:
        return jsonify({"error": "Missing 'prompt' in request."}), 400
    # Generate a response using the model. We limit the response length
    # to keep requests fast. Adjust `max_tokens` as needed.
    response = model.generate(prompt, max_tokens=256)
    return jsonify({"response": response.strip()})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)