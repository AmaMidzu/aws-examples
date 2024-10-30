import json
import boto3

client = boto3.client(service_name='bedrock-runtime')
prompt = "What should I do in San Francisco over a weekend?"
model_id = 'amazon.titan-text-lite-v1'

def lambda_handler(event, context):    
    payload = {
        'modelId': model_id,
        'inputText': prompt
    }
    
    response = client.invoke_model(**payload)
    
    model_response = json.loads(response['body'].read()['results'])
    return {
        'statusCode': 200,
        'body': model_response['results']
    }