import PyPDF2
import boto3
import io
import json
import urllib3

print('Loading function')

# Initialize AWS clients
s3 = boto3.client('s3')
sns = boto3.client('sns')

# OpenAI API settings
OPENAI_API_KEY = ""
OPENAI_API_URL = "https://api.openai.com/v1/completions"

def pdf_to_text(pdf_file):
    """Extract text from a PDF file."""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    return text

def lambda_handler(event, context):
      # Extract event data
    bucket = event['Records'][0]['s3']['bucket']['name']
    print("Bucket:", bucket)        
    key = event['Records'][0]['s3']['object']['key']
    print("Key:", key)
    event_name = event['Records'][0]['eventName']
    print("Event Name:", event_name)

    # Get object content
    response = s3.get_object(Bucket=bucket, Key=key)
    object_content = response['Body'].read()
    pdf_file = io.BytesIO(object_content)
    text = pdf_to_text(pdf_file)
    text = text[:250]
    print("Text:", text)

    return {
       'statusCode': 200,
       'statusMessage': 'OK'
    }
    
"""  # Prepare OpenAI API request
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo-instruct",
        "prompt": f"Summarize the following text: {text}",
        "max_tokens": 1000,
        "temperature": 0.5
    }
    print("Request data:", data)

    # Call OpenAI API
    http = urllib3.PoolManager()
    ai_response = http.request('POST', OPENAI_API_URL, headers=headers, body=json.dumps(data))

    # Parse JSON response
    response_data = json.loads(ai_response.data.decode('utf-8'))
    print("API response:", response_data)  # Print the response data for debugging

    # Check if the 'choices' key exists
    if 'choices' in response_data:
    # Check if the 'choices' list is not empty
        if len(response_data['choices']) > 0:
            # Check if the first choice has a 'text' key
            if 'text' in response_data['choices'][0]:
                summary = response_data["choices"][0]["text"]
            else:
                print("Error: The first choice does not have a 'text' key.")
        else:
            print("Error: The 'choices' list is empty.")
    else:
        print("Error: The 'choices' key does not exist.")
    print("Summary:", summary) """

    # TODO   https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-lambda-tutorial.html
    # publish message to write summary to RDS database
