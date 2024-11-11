def lambda_handler(event, context):
    print("Hello from Lambda 1") 
    return {"statusCode": 200, "body": "Hello World"} 
