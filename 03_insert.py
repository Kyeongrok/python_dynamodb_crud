import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('students')
table.put_item(Item={
    'class':2,
    'no':'5',
    'name':'경곡'
})
