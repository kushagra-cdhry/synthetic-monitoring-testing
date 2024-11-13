def lambda_handler(event, context):
    print("Hello from Lambda 4 latest") 
    return {"statusCode": 200, "body": "Hello from Lambda 4"} 