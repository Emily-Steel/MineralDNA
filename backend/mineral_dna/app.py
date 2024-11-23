import boto3
import json
import os
import psycopg2
from typing import Dict, Any
from mineral_dna.lib import calculate_mineral_DNA

HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "OPTIONS,POST",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
}


# Database connection setup
def get_db_connection():
    client = boto3.client("secretsmanager")
    secret_arn = os.getenv("POSTGRES_SECRET_ARN")
    secret = client.get_secret_value(SecretId=secret_arn)
    db_url = secret["SecretString"]
    return psycopg2.connect(db_url)


# Save DNA record to the database
def save_dna_record(user_id, names, surnames, dob, stones):
    query = """
    INSERT INTO dna_history (user_id, name, surname, dob, dna_data)
    VALUES (%s, %s, %s, %s, %s);
    """
    values = (user_id, " ".join(names), " ".join(surnames), dob, json.dumps(stones))

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, values)
        conn.commit()
    except Exception as e:
        print(f"Error saving DNA record: {e}")
    finally:
        conn.close()


def lambda_handler(event: Dict[str, Any], _: Any) -> Dict[str, Any]:
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

    user_id = body.get("userID")
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

    save_dna_record(user_id, names, surnames, dob, results)

    return {
        "statusCode": 200,
        "headers": HEADERS,
        "body": json.dumps({"stones": results}),
    }
