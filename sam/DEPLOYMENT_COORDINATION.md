# Coordinating Deployment: summafy-sam-app-lambda & summafy-state-machine-lambda

This guide explains how to coordinate deployment between your Lambda application code (`summafy-sam-app-lambda`) and your Terraform-managed infrastructure (`summafy-state-machine-lambda`).

---

## 1. Deploy Lambda Functions First (`summafy-sam-app-lambda`)

**Why?**  
The Step Functions state machine needs the ARNs of the Lambda functions, which are only available after deployment.

**How:**
```bash
sam build
sam deploy --guided
```
- This creates the Lambda functions and outputs their ARNs (usually as CloudFormation stack outputs).

---

## 2. Deploy Infrastructure and State Machine (`summafy-state-machine-lambda`)

**Why?**  
Your Terraform config references the Lambda ARNs (via CloudFormation stack outputs) to wire up the state machine tasks.

**How:**
```bash
terraform init
terraform apply
```
- Ensure your Terraform code is configured to read the correct CloudFormation stack outputs for the Lambda ARNs.
- This will create the Step Functions state machine, IAM roles, S3 triggers, etc., and link to the already-deployed Lambdas.

---

## 3. Update Workflow

- **If you update Lambda code:**
  - Redeploy with SAM.
  - If the function names or ARNs change (e.g., after a stack deletion/recreation), re-run Terraform to update the state machine with the new ARNs.

- **If you update the state machine or infrastructure:**
  - Update Terraform code.
  - Run `terraform apply` to apply changes.

---

## 4. (Optional) Automate with CI/CD
- Use scripts or CI/CD pipelines to automate the above steps.
- Ensure the SAM deployment step completes and outputs are available before running Terraform.

---

## 5. Monitoring & Observability

### Lambda Monitoring
- **CloudWatch Logs:** Each Lambda writes logs to CloudWatch. View logs in the AWS Console under CloudWatch > Log groups > `/aws/lambda/<function-name>`.
- **CloudWatch Metrics:** AWS provides metrics (Invocations, Duration, Errors, Throttles, etc.).
- **Alarms:** Set CloudWatch Alarms to alert on errors, duration, or throttles.
- **Tracing:** Enable AWS X-Ray for distributed tracing.

### Step Functions Monitoring
- **Execution History:** View execution steps, inputs, outputs, and errors in the Step Functions console.
- **CloudWatch Logs:** Enable logging for the state machine to send execution data to CloudWatch Logs.
- **CloudWatch Metrics:** Metrics for executions started, succeeded, failed, and timed out.
- **Alarms:** Set alarms for failed or timed-out executions.
- **Tracing:** Enable AWS X-Ray for state machine executions.

### CI/CD Monitoring
- **Pipeline Status:** Monitor pipeline runs in your CI/CD platform.
- **Notifications:** Set up notifications for failed deployments or tests.

### Example: Terraform Snippet for Step Functions Logging

```hcl
resource "aws_cloudwatch_log_group" "state_machine_logs" {
  name              = "/aws/vendedlogs/state-machine-logs"
  retention_in_days = 14
}

resource "aws_sfn_state_machine" "state_machine" {
  # ... other properties ...
  logging_configuration {
    level = "ALL"
    include_execution_data = true
    destinations {
      cloudwatch_logs_log_group {
        log_group_arn = aws_cloudwatch_log_group.state_machine_logs.arn
      }
    }
  }
}
```

---

## Summary Table

| Step                 | Tool      | Directory                    | Command(s)                        |
|----------------------|-----------|------------------------------|------------------------------------|
| Deploy Lambdas       | SAM CLI   | summafy-sam-app-lambda       | `sam build && sam deploy`          |
| Deploy State Machine | Terraform | summafy-state-machine-lambda | `terraform init && terraform apply`|

---

## Summary Table (Extended)

| Component       | Logs                | Metrics             | Alarms            | Tracing   |
|-----------------|---------------------|---------------------|-------------------|-----------|
| Lambda          | CloudWatch Logs     | CloudWatch Metrics  | CloudWatch Alarms | X-Ray     |
| Step Functions  | CloudWatch Logs     | CloudWatch Metrics  | CloudWatch Alarms | X-Ray     |
| CI/CD Pipeline  | CI/CD Platform Logs | CI/CD Metrics       | CI/CD Alerts      | N/A       |

---

**Key Point:**  
Always deploy/update Lambda functions first, then run Terraform to wire up or update the state machine and triggers.

---

If you want a sample deployment script or more details on output wiring, check with your infrastructure or DevOps specialist, or ask for further guidance here!

For more details or to enable advanced monitoring (e.g., custom metrics, X-Ray), see AWS documentation or ask for tailored guidance!
