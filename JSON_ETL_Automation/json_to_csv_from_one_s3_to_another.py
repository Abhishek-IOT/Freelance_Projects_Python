import boto3
import pandas as pd
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Hardcoded S3 paths
    source_bucket = 'Source_Bucket_Name'
    source_key = 'RAW/Customer.json'
    
    destination_bucket = 'Target_Bucket_Name'
    destination_key = 'CURATED/Customer.csv'

    try:
        # Read JSON from S3
        response = s3.get_object(Bucket=source_bucket, Key=source_key)
        json_bytes = response['Body'].read()
        
        # Load into pandas
        df = pd.read_json(io.BytesIO(json_bytes))
        
        # Convert to CSV in memory
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)

        # Upload to S3
        s3.put_object(
            Bucket=destination_bucket,
            Key=destination_key,
            Body=csv_buffer.getvalue().encode('utf-8')
        )

        return {
            'statusCode': 200,
            'body': f'CSV uploaded to s3://{destination_bucket}/{destination_key}'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
