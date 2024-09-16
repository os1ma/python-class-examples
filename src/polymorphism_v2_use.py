from src.polymorphism_v1 import BaseLLM, OpenAILLM


class MySuperChatApplication:
    def __init__(self, llm: BaseLLM) -> None:
        self.llm = llm

    def chat(self, user_input: str) -> str:
        # 実際にはこのあたりでもっと色々処理する
        return self.llm.predict(user_input)


def main() -> None:
    # LLMを設定によって変更したりできる
    llm = OpenAILLM(api_key="dummy", model_name="model_name")
    app = MySuperChatApplication(llm=llm)
    response = app.chat("こんにちは")
    print(response)


if __name__ == "__main__":
    main()
