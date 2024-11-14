import json
from typing import Dict, Any
from backend.mineral_dna.lib import calculate_mineral_DNA
from aws_lambda_powertools.utilities.typing import LambdaContext


def lambda_handler(event: Dict[str, Any], _: LambdaContext) -> Dict[str, str]:
    body_content = event.get("body", "{}")
    
    # If body_content is a string, parse it as JSON
    if isinstance(body_content, str):
        try:
            body = json.loads(body_content)
        except json.JSONDecodeError:
            body = {}  # Fallback in case of JSON parsing error
    else:
        body = body_content  # If it's already a dict, use it directly

    names = body.get("names", "").split()
    surnames = body.get("surnames", "").split()
    dob = body.get("dob", "")

    if len(names) == 0 or len(surnames) == 0 or len(dob.split("/")) != 3:
        return {
            "statusCode": 400,
            "body": f"Invalid request body (names:'{names}', surnames:'{surnames}', dob: '{dob}'"
        }

    results = calculate_mineral_DNA(names, surnames, dob)

    return {
        "statusCode": 200,
        "body": {
            "stones": results
        }
    }