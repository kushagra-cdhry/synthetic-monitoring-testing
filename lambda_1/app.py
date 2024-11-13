def lambda_handler(event, context):
    print("Hello from Lambda 1 new") 
    return {"statusCode": 200, "body": "Hello from Lambda 1 Neww"} 

