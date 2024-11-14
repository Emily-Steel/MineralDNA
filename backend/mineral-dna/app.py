import json
from typing import Dict
from mineral_DNA import calculate_mineral_DNA
from aws_lambda_powertools.utilities.typing import LambdaContext


def lambda_handler(event: Dict[str, str], _: LambdaContext) -> Dict[str, str]:
    body = json.loads(event.get("body", "{}"))
    names = body.get("names", "").split()
    surnames = body.get("surnames", "").split()
    dob = body.get("dob", "")

    results: list = calculate_mineral_DNA(names, surnames, dob)

    return {
        "statusCode": 200,
        "body": json.dumps(results)
    }