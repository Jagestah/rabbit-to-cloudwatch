# rabbit-cloudwatch
Pull all rabbit queue sizes that don't start with 'amq' and push to AWS cloudwatch every 5 minutes.

## Environment Variables

- RABBIT_MQ_URL
- RABBIT_MQ_USERNAME
- RABBIT_MQ_PASSWORD
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
