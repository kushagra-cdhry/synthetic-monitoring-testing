def lambda_handler(event, context):
    print("Hello from Lambda 2 ---- update 1") 
    return {"statusCode": 200, "body": "Hello from Lambda 2"} 