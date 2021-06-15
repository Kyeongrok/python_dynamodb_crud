import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('students')
r = table.query(
    KeyConditionExpression=Key('class').eq(2) & Key('no').eq(4)
)
print(r)
