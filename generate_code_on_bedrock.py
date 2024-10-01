import boto3
import json

from botocore.exceptions import ClientError

brt = boto3.client("bedrock-runtime")

model_id = "amazon.titan-text-express-v1"

prompt = """You are a Python developer. Write a Python function to solve 
the following problem:

Given an array of integers nums and an integer target, return indices 
of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and 
you may not use the same element twice.

You can return the answer in any order."""


request = {
    "inputText": prompt,
    "textGenerationConfig": {
        "maxTokenCount": 512,
        "temperature": 0.9,
        "topP": 0.9
    },
}

request = json.dumps(request)

try:
    response = brt.invoke_model(modelId=model_id, body=request)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)

model_response = json.loads(response["body"].read())

response_text = model_response["results"][0]["outputText"]
print(response_text)