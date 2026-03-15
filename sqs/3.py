import boto3

alarm = boto3.client('cloudwatch', endpoint_url="http://localhost:4566")

alarm.delete_alarms(
  AlarmNames=['Web_Server_CPU_Utilization'],
)