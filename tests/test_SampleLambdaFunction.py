import json
from functions.lambda_function import lambda_handler


def test_lambda_handler():
    test_event = {
        "body": json.dumps(
            {
                "input": "こんにちは。",
            }
        )
    }

    result = lambda_handler(test_event, None)
    body_content = json.loads(result["body"])

    print(json.dumps(body_content, ensure_ascii=False, indent=2))

    assert isinstance(result, dict), "結果は辞書型であるべき"
    assert "statusCode" in result, "結果にはstatusCodeが含まれるべき"
    assert result["statusCode"] == 200, "ステータスコードは200であるべき"
