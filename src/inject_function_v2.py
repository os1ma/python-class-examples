from abc import ABC, abstractmethod

from anthropic import Anthropic
from openai import OpenAI


class BaseLLM(ABC):
    @abstractmethod
    def predict(self, prompt: str) -> str | None:
        pass


class OpenAILLM(BaseLLM):
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    def predict(self, prompt: str) -> str | None:
        client = OpenAI()
        completion = client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
        )
        return completion.choices[0].message.content


class AnthropicLLM(BaseLLM):
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    def predict(self, prompt: str) -> str:
        client = Anthropic()
        message = client.messages.create(
            model=self.model_name,
            max_tokens=100,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text
