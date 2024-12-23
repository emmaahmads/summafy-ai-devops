def lambda_handler(event, context):
    # Extract text from step function input
    text = event.get('text')
    if not text:
        return {
            'statusCode': 400,
            'statusMessage': 'No text provided in event'
        }

    # # Prepare OpenAI API request
    # headers = {
    #     "Authorization": f"Bearer {OPENAI_API_KEY}", 
    #     "Content-Type": "application/json"
    # }
    # data = {
    #     "model": "gpt-3.5-turbo-instruct",
    #     "prompt": f"Summarize the following text: {text}",
    #     "max_tokens": 1000,
    #     "temperature": 0.5
    # }
    # print("Request data:", data)

    # # Call OpenAI API
    # http = urllib3.PoolManager()
    # ai_response = http.request('POST', OPENAI_API_URL, headers=headers, body=json.dumps(data))

    # # Parse JSON response
    # response_data = json.loads(ai_response.data.decode('utf-8'))
    # print("API response:", response_data)

    # # Extract summary from response
    # summary = None
    # if ('choices' in response_data and 
    #     len(response_data['choices']) > 0 and
    #     'text' in response_data['choices'][0]):
    #     summary = response_data["choices"][0]["text"]
    # else:
    #     return {
    #         'statusCode': 500,
    #         'statusMessage': 'Failed to get summary from OpenAI API'
    #     }

    # Return summary for next step in workflow
    return {
        'statusCode': 200,
        'statusMessage': 'OK',
        'summary': text
    }
