# variable "bucket_name" {
#   description = "The name of the S3 bucket to use as the source bucket."
#   type        = string
# }

data "aws_s3_bucket" "source_bucket" {
  bucket = "superumi-summafy-123"
}

data "aws_cloudformation_stack" "functions" {
  name = "summafy-lambdas"
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = data.aws_s3_bucket.source_bucket.id
  # eventbridge = true
}

resource "aws_sfn_state_machine" "state_machine" {
  name     = "IngestorStateMachine"
  role_arn = "arn:aws:iam::120569638976:role/StepFunctionExecutionRole"

  definition = jsonencode({
    Comment = "The state machines of the pdf processing"
    StartAt = "Ingestor"
    States = {
      Ingestor = {
        Type       = "Task"
        Resource   = data.aws_cloudformation_stack.functions.outputs["SummafyIngestorFunction"]
        End = true
      },
    }
  })
}

# resource "aws_cloudwatch_event_rule" "s3_event_rule" {
#   name        = "S3EventRule"
#   description = "Rule to trigger Step Function on S3 create event"
#   event_pattern = jsonencode({
#     source = ["aws.s3"]
#     detail-type = ["Object Created"]
#     detail = {
#       bucket = {
#         name = [data.aws_s3_bucket.source_bucket.bucket]
#       }
#     }
#   })
# }

// specify a target for a cw event
# resource "aws_cloudwatch_event_target" "start_sm" {
#   rule       = aws_cloudwatch_event_rule.s3_event_rule.name
#   arn        = aws_sfn_state_machine.state_machine.arn
#   role_arn   = aws_iam_role.cloudwatch_event_role.arn
# }

// allows StepFunction to invoke Lambda functions

# resource "aws_lambda_permission" "allow_cloudwatch_to_invoke" {
#   statement_id  = "AllowExecutionFromCloudWatch"
#   action        = "lambda:InvokeFunction"
#   function_name = aws_sfn_state_machine.state_machine.name
#   principal     = "events.amazonaws.com"
#   source_arn    = aws_cloudwatch_event_rule.s3_event_rule.arn
# }

