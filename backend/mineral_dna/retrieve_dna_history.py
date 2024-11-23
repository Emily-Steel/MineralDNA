import boto3
import json
import os
import psycopg2
from psycopg2.extras import DictCursor
from typing import Dict, Any

HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "OPTIONS,GET",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
}


# Database connection setup
def get_db_connection():
    client = boto3.client("secretsmanager")
    secret_arn = os.getenv("POSTGRES_SECRET_ARN")
    secret = client.get_secret_value(SecretId=secret_arn)
    db_url = secret["SecretString"]
    return psycopg2.connect(db_url)


def lambda_handler(event: Dict[str, Any], _: Any) -> Dict[str, str]:
    if event["httpMethod"] == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": HEADERS,
        }

    user_id = event.get("queryStringParameters", {}).get("userID")
    if not user_id:
        return {
            "statusCode": 400,
            "headers": HEADERS,
            "body": json.dumps({"error": "Missing userID"}),
        }

    query = "SELECT * FROM dna_history WHERE user_id = %s ORDER BY created_at DESC;"
    conn = get_db_connection()
    try:
        with conn.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute(query, (user_id,))
            records = cursor.fetchall()
        dna_history = [dict(record) for record in records]
        return {
            "statusCode": 200,
            "headers": HEADERS,
            "body": json.dumps({"dnaHistory": dna_history}),
        }
    except Exception as e:
        print(f"Error fetching DNA history: {e}")
        return {
            "statusCode": 500,
            "headers": HEADERS,
            "body": json.dumps({"error": str(e)}),
        }
    finally:
        conn.close()
