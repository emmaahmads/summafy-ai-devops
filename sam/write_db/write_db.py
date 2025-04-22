import json
import psycopg2
import os


def lambda_handler(event, context):
    # Extract data from the event
    data = event.get('summary')
    print("Received data:", data)
    
    # Database connection parameters
    db_host = os.environ['RDS_DB_URL']
    db_name = "summafy"
    db_user = os.environ['RDS_DB_USER']
    db_password = os.environ['RDS_DB_PASSWORD']
    print("Database connection parameters:")
    print("  Host:", db_host)
    print("  Name:", db_name)
    print("  User:", db_user)
    print("  Password:", db_password)
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    
    # Create a cursor object
    cur = conn.cursor()
    
    # Insert data into the table
    insert_query = """
        INSERT INTO summary (
            doc_id,
            param1,
            param2,
            summary
            ) VALUES (
            %s, %s, %s, %s
            ) RETURNING id, doc_id, param1, param2, summary
        """
    cur.execute(insert_query, (2, True, True, data))
    
    # Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cur.close()
    conn.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data written to database successfully!')
    }