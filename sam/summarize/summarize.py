def lambda_handler(event, context):
    # Extract text from step function input
    text = event.get('text')
    return {
        'statusCode': 200,
        'statusMessage': 'OK',
        'summary': text
    }
