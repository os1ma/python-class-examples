from dotenv import load_dotenv

from src.inject_function_v2 import AnthropicLLM, BaseLLM, OpenAILLM

load_dotenv(override=True)


class MySuperChatApplication:
    def __init__(self, llm: BaseLLM) -> None:
        self.llm = llm

    def chat(self, user_input: str) -> str | None:
        # 実際にはこのあたりでもっと色々処理する
        return self.llm.predict(user_input)


def main() -> None:
    openai_llm = OpenAILLM(model_name="gpt-4o-mini")
    app = MySuperChatApplication(llm=openai_llm)
    response = app.chat("こんにちは")
    print(response)

    anthropic_llm = AnthropicLLM(model_name="claude-3-haiku-20240307", max_tokens=100)
    app = MySuperChatApplication(llm=anthropic_llm)
    response = app.chat("こんにちは")
    print(response)


if __name__ == "__main__":
    main()
