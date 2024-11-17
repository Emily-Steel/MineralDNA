import json
from typing import Dict, Any
from lib import calculate_mineral_DNA

HEADERS = {
    "Access-Control-Allow-Origin": "http://localhost:5173",
    "Access-Control-Allow-Methods": "OPTIONS,POST",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
}


def lambda_handler(event: Dict[str, Any], _: Any) -> Dict[str, str]:
    if event["httpMethod"] == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": HEADERS,
        }

    print(json.dumps(event, indent=2))
    body_content = event.get("body", "{}")

    # If body_content is a string, parse it as JSON
    if isinstance(body_content, str):
        try:
            body = json.loads(body_content)
        except json.JSONDecodeError:
            body = {}  # Fallback in case of JSON parsing error
    else:
        body = body_content  # If it's already a dict, use it directly

    if body is None or not isinstance(body, dict):
        return {
            "statusCode": 400,
            "headers": HEADERS,
            "body": json.dumps(
                {"error": "Empty or invalid body. Expected names, surnames, and dob"}
            ),
        }
    names = body.get("names", "").split()
    surnames = body.get("surnames", "").split()
    dob = body.get("dob", "")

    if len(names) == 0 or len(surnames) == 0 or len(dob.split("/")) != 3:
        return {
            "statusCode": 400,
            "headers": HEADERS,
            "body": json.dumps(
                {
                    "error": f"Invalid request body (names:'{names}', surnames:'{surnames}', dob: '{dob}'"
                }
            ),
        }

    results = calculate_mineral_DNA(names, surnames, dob)

    return {
        "statusCode": 200,
        "headers": HEADERS,
        "body": json.dumps({"stones": results}),
    }
