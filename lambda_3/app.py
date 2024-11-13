def lambda_handler(event, context):
    print("Hello from Lambda 3 latestt") 
    return {"statusCode": 200, "body": "Hello from Lambda 3"} 