from abc import ABC, abstractmethod


class BaseLLM(ABC):
    @abstractmethod
    def predict(self, prompt: str) -> str:
        pass


class OpenAILLM(BaseLLM):
    def __init__(self, api_key: str, model_name: str) -> None:
        self.api_key = api_key
        self.model_name = model_name

    def predict(self, prompt: str) -> str:
        # 実際にはここでAPIを呼び出す
        return "OpenAIの言語モデルが返したテキスト"


class AnthropicLLM(BaseLLM):
    def __init__(self, api_key: str, model_name: str) -> None:
        self.api_key = api_key
        self.model_name = model_name

    def predict(self, prompt: str) -> str:
        # 実際にはここでAPIを呼び出す
        return "Anthropicの言語モデルが返したテキスト"
