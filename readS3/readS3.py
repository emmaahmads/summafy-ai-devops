import PyPDF2
import boto3
import re
import io
import json
import urllib3

print('Loading function')

# Initialize AWS clients
s3 = boto3.client('s3')

def clean_text(text):
   cleaned_text = re.sub(r' +', ' ', text)
   # Replace newline characters with spaces
   cleaned_text = cleaned_text.replace('\n', ' ')
   # Remove spaces around hyphens
   cleaned_text = re.sub(r'\s*-\s*', '', cleaned_text)
   return cleaned_text

def pdf_to_text(pdf_file):
    print("pdf_file:", pdf_file)

    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()
    
    cleaned_text = clean_text(text)    
    return cleaned_text

def lambda_handler(event, context):
    try:
        # Extract event data
        bucket = event['detail']['bucket']['name']
        key = event['detail']['object']['key']

        # Get object content
        response = s3.get_object(Bucket=bucket, Key=key)
        object_content = response['Body'].read()
    except Exception as e:
        return {
            'statusCode': 500,
            'statusMessage': 'Internal Server Error',
            'error': str(e)
        }

    try:    
        # Check if file is PDF by looking at magic numbers
        if object_content.startswith(b'%PDF'):
            pdf_file = io.BytesIO(object_content)
            text = pdf_to_text(pdf_file)
            text = text[:250]
            if text == "":
                text = "File is not a text-based PDF"      
        else:
            text = "File is not a text-based PDF"
        print("Text:", text)      
        return {
            'statusCode': 200,
            'statusMessage': 'OK',
            'text': text
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'statusMessage': 'Error reading file',
            'error': str(e)
        }

    