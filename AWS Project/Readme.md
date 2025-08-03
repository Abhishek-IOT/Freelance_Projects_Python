# Real-Time Customer Feedback Pipeline using AWS (S3, Lambda, Redshift).

This project demonstrates a real-time serverless data pipeline that ingests raw JSON customer feedback, transforms it into CSV, 
and loads it into Amazon Redshift for analytical querying. The entire flow is automated using AWS-native services.

# Architecture

<img width="717" height="349" alt="image" src="https://github.com/user-attachments/assets/22540c79-10b6-4edc-a0d7-23ee15e5533c" />



# 📝 Project Flow
1)Upload JSON to s3.
2)Lambda Trigger: Automatically triggered when a new file arrives
3)Reads JSON
4)Converts to structured CSV using Pandas
5)Uploads to s3
6)Scheduled COPY to Redshift
7)Every 5 minutes, EventBridge triggers a Redshift query.
8)COPY command loads data from curated S3 to Redshift table MARKET.Cust
