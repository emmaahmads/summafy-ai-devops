import json
import psycopg2
import os


def lambda_handler(event, context):
    # # Extract data from the event
    # data = event['data']
    
    # # Database connection parameters
    # db_host = os.environ['RDS_DB_URL']
    # db_name = "summafy"
    # db_user = os.environ['RDS_DB_USER']
    # db_password = os.environ['RDS_DB_PASSWORD']
    
    # # Connect to the PostgreSQL database
    # conn = psycopg2.connect(
    #     host=db_host,
    #     database=db_name,
    #     user=db_user,
    #     password=db_password
    # )
    
    # # Create a cursor object
    # cur = conn.cursor()
    
    # # Insert data into the table
    # insert_query = """
    # INSERT INTO your_table_name (column1, column2, column3)
    # VALUES (%s, %s, %s)
    # """
    # cur.execute(insert_query, (data['column1'], data['column2'], data['column3']))
    
    # # Commit the transaction
    # conn.commit()
    
    # # Close the cursor and connection
    # cur.close()
    # conn.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data written to database successfully!')
    }