import boto3
import json
from datetime import datetime
from botocore.exceptions import ClientError

# AWS Configuration
S3_BUCKET = 'rawingestion007'
S3_KEY = 'Customer.json'
KINESIS_STREAM = 'data_stream'
AWS_REGION = 'us-east-1'  # Change if needed

def get_aws_session():
    """Create AWS session with explicit credentials"""
    # Option 1: Use existing IAM role (recommended for EC2/Cloud9)
    # session = boto3.Session(region_name=AWS_REGION)
    
    # Option 2: Use explicit credentials (for local testing)
    session = boto3.Session(
        region_name=AWS_REGION,
        aws_access_key_id='****',    # Replace with your key
        aws_secret_access_key='****' # Replace with your secret
    )
    return session

def read_json_from_s3(session):
    """Read JSON file from S3 with error handling"""
    s3 = session.client('s3')
    try:
        response = s3.get_object(Bucket=S3_BUCKET, Key=S3_KEY)
        data = json.loads(response['Body'].read().decode('utf-8'))
        print(f"✅ Successfully read {len(data)} records from S3")
        return data
    except ClientError as e:
        if e.response['Error']['Code'] == 'AccessDenied':
            print("❌ Access Denied to S3. Please check:")
            print(f"- Bucket name: {S3_BUCKET}")
            print(f"- IAM permissions: s3:GetObject")
            print(f"- Bucket policy allows your user/role")
        else:
            print(f"❌ S3 Error: {str(e)}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error reading S3: {str(e)}")
        return None

def send_to_kinesis(session, records):
    """Send records to Kinesis with error handling"""
    kinesis = session.client('kinesis')
    success_count = 0
    
    for record in records:
        try:
            response = kinesis.put_record(
                StreamName=KINESIS_STREAM,
                Data=json.dumps(record),
                PartitionKey=str(record['user_id'])
            )
            success_count += 1
            print(f"📨 Sent record {record['user_id']} (Seq: {response['SequenceNumber'][:10]}...)")
        except ClientError as e:
            if e.response['Error']['Code'] == 'AccessDenied':
                print("❌ Access Denied to Kinesis. Please check:")
                print(f"- Stream name: {KINESIS_STREAM}")
                print(f"- IAM permissions: kinesis:PutRecord")
            else:
                print(f"❌ Kinesis Error: {str(e)}")
        except Exception as e:
            print(f"❌ Failed to send record {record['user_id']}: {str(e)}")
    
    return success_count

def main():
    print(f"🚀 Starting process at {datetime.now().isoformat()}")
    print(f"📂 Reading from s3://{S3_BUCKET}/{S3_KEY}")
    
    # Create authenticated session
    session = get_aws_session()
    
    # Step 1: Read data from S3
    records = read_json_from_s3(session)
    if not records:
        return
    
    # Step 2: Send to Kinesis
    print(f"📤 Sending to Kinesis stream: {KINESIS_STREAM}")
    success_count = send_to_kinesis(session, records)
    
    # Results
    print("\n🔍 Processing complete")
    print(f"📊 Total records: {len(records)}")
    print(f"✅ Successfully sent: {success_count}")
    print(f"❌ Failed: {len(records) - success_count}")

if __name__ == "__main__":
    main()