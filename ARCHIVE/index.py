import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoItems')

def lambda_handler(event, context):
    method = event['httpMethod']

    if method == 'POST':
        data = json.loads(event['body'])
        item = {
            'id': str(uuid.uuid4()),
            'task': data['task']
        }
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }

    elif method == 'GET':
        response = table.scan()
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }

    elif method == 'DELETE':
        item_id = event['queryStringParameters']['id']
        table.delete_item(Key={'id': item_id})
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item deleted'})
        }

    else:
        return {
            'statusCode': 405,
            'body': 'Method Not Allowed'
        }
