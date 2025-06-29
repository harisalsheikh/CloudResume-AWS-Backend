import boto3
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ResumeVisitorCounter")


def lambda_handler(event, context):
    try:
        print("Event received:", event)

        response = table.update_item(
            Key={"id": "visitor-count"},
            UpdateExpression="SET #c = if_not_exists(#c, :start) + :inc",
            ExpressionAttributeNames={"#c": "count"},
            ExpressionAttributeValues={":inc": 1, ":start": 0},
            ReturnValues="UPDATED_NEW",
        )

        new_count = response["Attributes"]["count"]
        print("New count is:", new_count)

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json",
            },
            "body": json.dumps({"count": int(new_count)}),
        }

    except Exception as e:
        print("Error occurred:", str(e))
        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "Could not update counter"}),
        }
