### 2. Create an S3 Bucket
- Bucket name: `demo-staging`
- Enable **Bucket owner enforced** (ACLs disabled).
- Add a **lifecycle rule** to transition objects to **Glacier after 1 day**.

---

### 3. Create the Lambda Function
- Function name: `ExportECSLogsToS3`
- Runtime: `Python 3.13`
- Memory: `128 MB`


### Create a CloudWatch Subscription Filter

  - Source: /ecs/demo-staging log group
  - Destination: ExportECSLogsToS3 Lambda function
  - Filter name: DemoStagingToS3
  - Filter pattern: leave empty (matches all logs)
