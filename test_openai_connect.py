import pytest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from openai_connect import client

def test_openai_api_key():
    assert os.getenv("OPENAI_API_KEY"), "API key should be set in environment"

def test_openai_chat_completion():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Test"}]
    )
    assert response.choices[0].message.content, "Response should contain content"
