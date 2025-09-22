# ecs-cloudwatch-lambda-s3-glacier
This project demonstrates how to automatically export Amazon ECS container logs (from CloudWatch Logs) into an Amazon S3 bucket for long-term storage and archival. The solution uses an AWS Lambda function triggered by a CloudWatch Logs subscription filter to decode, process, and upload logs into S3 in JSON format.
