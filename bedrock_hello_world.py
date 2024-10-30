import boto3
import json

client = boto3.client('bedrock')

def invoke_model(prompt, streaming=False):
    payload = {
        'modelId': <use your model id>,
        'inputText': prompt
    }
    
    if streaming:
        response = client.invoke_model_streaming(
            **payload
        )
    else:
        response = client.invoke_model(
            **payload
        )
    
    return response

def main():
    prompt = "What should I do in San Francisco over a weekend?"
    
    # No streaming option
    print("Invoking model without streaming...")
    response = invoke_model(prompt)
    print("Response:", json.loads(response['body']))
  
    # Streaming option
    print("Invoking model with streaming...")
    streaming_response = invoke_model(prompt, streaming=True)
    for event in streaming_response['events']:
        print("Streaming response:", event['body'])

if __name__ == "__main__":
    main()