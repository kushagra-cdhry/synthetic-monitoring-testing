def lambda_handler(event, context):
    print("Hello from Lambda 1-----update2") 
    return {"statusCode": 200, "body": "Hello from Lambda 1"} 
