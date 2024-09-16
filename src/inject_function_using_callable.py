from typing import Callable


def chat(predict_func: Callable[[str], str], user_input: str) -> str:
    # 実際にはこのあたりでもっと色々処理する
    return predict_func(user_input)


def my_predict_func(prompt: str) -> str:
    return "OpenAIの言語モデルが返したテキスト"


def main() -> None:
    response = chat(predict_func=my_predict_func, user_input="こんにちは")
    print(response)


if __name__ == "__main__":
    main()
