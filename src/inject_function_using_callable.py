# mypy: disable-error-code="union-attr"

from typing import Callable

from anthropic import Anthropic
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)


def predict_by_openai(prompt: str) -> str | None:
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content


def predict_by_anthropic(prompt: str) -> str | None:
    client = Anthropic()
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=100,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def chat(predict_func: Callable[[str], str | None], user_input: str) -> str | None:
    # 実際にはこのあたりでもっと色々処理する
    return predict_func(user_input)


def main() -> None:
    response = chat(predict_func=predict_by_openai, user_input="こんにちは")
    print(response)

    response = chat(predict_func=predict_by_anthropic, user_input="こんにちは")
    print(response)


if __name__ == "__main__":
    main()
