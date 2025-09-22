import boto3
import gzip
import json
import base64
from datetime import datetime

s3 = boto3.client("s3")
BUCKET_NAME = "demo-staging"

def lambda_handler(event, context):
  # Decode CloudWatch Logs payload
  data = base64.b64decode(event["awslogs"]["data"])
  decompressed = gzip.decompress(data)
  log_data = json.loads(decompressed)

  log_group = log_data["logGroup"].strip("/")
  log_stream = log_data["logStream"].replace("/", "-")
  timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")

  # Construct S3 filename
  filename = f"{log_group}/{log_stream}-{timestamp}.json"

  # Upload to S3
  s3.put_object(
      Bucket=BUCKET_NAME,
      Key=filename,
      Body=json.dumps(log_data, indent=2).encode("utf-8")
  )

  print(f"✅ Logs uploaded to s3://{BUCKET_NAME}/{filename}")
  return {"status": "success"}
