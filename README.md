#  Export ECS Logs from CloudWatch to Amazon S3 (with Lambda & Glacier)

This project shows how to stream ECS container logs from **CloudWatch Logs** → **AWS Lambda** → **Amazon S3** and then archive them to **Glacier** automatically.


**WorkFlow**

Workflow: ECS → CloudWatch → Lambda → S3 → Glacier

##  Steps to Set Up

### 1. ECS Service Logging
- ECS service name: `demo-staging`
- Logs pushed into CloudWatch Logs:
