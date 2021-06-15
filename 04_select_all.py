import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('students')
r = table.scan()
print(r)

