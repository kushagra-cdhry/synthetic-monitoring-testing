def lambda_handler(event, context):
    print("Hello from Lambda 5") 
    return {"statusCode": 200, "body": "Hello World"} 