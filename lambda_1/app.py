def lambda_handler(event, context):
    print("Hello from Lambda 1-----update1") 
    return {"statusCode": 200, "body": "Hello from Lambda 1"} 