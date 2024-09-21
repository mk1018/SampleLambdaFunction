import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def lambda_handler(event, context):
    body = json.loads(event["body"])

    input = body["input"]

    messages = [
        {
            "role": "system",
            "content": "ユーザーの質問に適当に答えてください。",
        },
        {
            "role": "user",
            "content": (f"ユーザーの質問：{input}"),
        },
    ]

    response = client.chat.completions.create(model="gpt-4o", messages=messages)

    astrology_result = (
        response.choices[0].message.content if response.choices else "No result found."
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"result": astrology_result}),
    }


if __name__ == "__main__":
    lambda_handler(None, None)
