### 2. Create an S3 Bucket
- Bucket name: `demo-staging`
- Enable **Bucket owner enforced** (ACLs disabled).
- Add a **lifecycle rule** to transition objects to **Glacier after 1 day**.

---

### 3. Create the Lambda Function
- Function name: `ExportECSLogsToS3`
- Runtime: `Python 3.13`
- Memory: `128 MB`
