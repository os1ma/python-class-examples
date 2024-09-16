from src.polymorphism_v1 import BaseLLM, OpenAILLM


def chat(llm: BaseLLM, user_input: str) -> str:
    # 実際にはこのあたりでもっと色々処理する
    return llm.predict(user_input)


def main() -> None:
    # LLMを設定によって変更したりできる
    llm = OpenAILLM(api_key="dummy", model_name="model_name")
    response = chat(llm=llm, user_input="こんにちは")
    print(response)


if __name__ == "__main__":
    main()
