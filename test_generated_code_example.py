import boto3
import json

from botocore.exceptions import ClientError

brt = boto3.client("bedrock-runtime")

model_id = "amazon.titan-text-express-v1"

prompt = """Generate a pytest test for the following Python function:

def two_sum(nums, target):
    nums_len = len(nums)
    for i in range(nums_len):
        for j in range(i + 1, nums_len):
            if nums[i] + nums[j] == target:
                return [i, j]
"""


request = {
    "inputText": prompt,
    "textGenerationConfig": {
        "maxTokenCount": 512,
        "temperature": 0,
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