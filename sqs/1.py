import boto3

sqs = boto3.resource('sqs',endpoint_url="http://localhost:4566")

queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

print(queue.url)