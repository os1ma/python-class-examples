from dotenv import load_dotenv

from src.inject_function_v2 import AnthropicLLM, BaseLLM, OpenAILLM

load_dotenv(override=True)


def chat(llm: BaseLLM, user_input: str) -> str | None:
    # 実際にはこのあたりでもっと色々処理する
    return llm.predict(user_input)


def main() -> None:
    openai_llm = OpenAILLM(model_name="gpt-4o-mini")
    response = chat(llm=openai_llm, user_input="こんにちは")
    print(response)

    anthropic_llm = AnthropicLLM(model_name="claude-3-haiku-20240307")
    response = chat(llm=anthropic_llm, user_input="こんにちは")
    print(response)


if __name__ == "__main__":
    main()
