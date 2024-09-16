from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)


def predict(prompt: str) -> str | None:
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content


def chat(user_input: str) -> str | None:
    # 実際にはこのあたりでもっと色々処理する
    return predict(user_input)


def main() -> None:
    response = chat(user_input="こんにちは")
    print(response)


if __name__ == "__main__":
    main()
