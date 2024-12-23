import PyPDF2
import boto3
import io
import json
import urllib3

print('Loading function')

# Initialize AWS clients
s3 = boto3.client('s3')

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
       'statusMessage': 'OK',
       'text': textS
    }