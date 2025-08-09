import boto3
import time
from datetime import datetime

def lambda_handler(event, context):
    # Initialize CloudWatch Logs client
    logs = boto3.client('logs')
    
    # Constants
    LOG_GROUP = '/aws/lambda/my-log-group'
    LOG_STREAM = 'my-log-stream'
    
    try:
        # 1. Create Log Group (if doesn't exist)
        try:
            logs.create_log_group(logGroupName=LOG_GROUP)
            print(f"Created log group: {LOG_GROUP}")
        except logs.exceptions.ResourceAlreadyExistsException:
            print(f"Log group exists: {LOG_GROUP}")
            pass
        
        # 2. Create Log Stream (if doesn't exist)
        try:
            logs.create_log_stream(
                logGroupName=LOG_GROUP,
                logStreamName=LOG_STREAM
            )
            print(f"Created log stream: {LOG_STREAM}")
        except logs.exceptions.ResourceAlreadyExistsException:
            print(f"Log stream exists: {LOG_STREAM}")
            pass
        
        # 3. Insert Log Record (immutable)
        timestamp = int(time.time() * 1000)
        log_event = {
            'logGroupName': LOG_GROUP,
            'logStreamName': LOG_STREAM,
            'logEvents': [
                {
                    'timestamp': timestamp,
                    'message': f"New log entry at {datetime.now().isoformat()}"
                }
            ]
        }
        
        # Get sequence token for existing stream
        response = logs.describe_log_streams(
            logGroupName=LOG_GROUP,
            logStreamNamePrefix=LOG_STREAM
        )
        
        if 'uploadSequenceToken' in response['logStreams'][0]:
            log_event['sequenceToken'] = response['logStreams'][0]['uploadSequenceToken']
        
        # Put the log event
        logs.put_log_events(**log_event)
        print("Successfully inserted log record")
        
        return {
            'statusCode': 200,
            'body': 'Log inserted successfully',
            'log_group': LOG_GROUP,
            'log_stream': LOG_STREAM,
            'timestamp': timestamp
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise