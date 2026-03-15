import boto3

alarm = boto3.client('cloudwatch',endpoint_url="http://localhost:4566")

alarm.put_metric_alarm(
    AlarmName='Web_Server_CPU_Utilization',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=60,
    Statistic='Average',
    Threshold=70.0,
    ActionsEnabled=False,
    AlarmDescription='Alarm when server CPU exceeds 70%')


page = alarm.get_paginator('describe_alarms')
for response in page.paginate(StateValue='INSUFFICIENT_DATA'):
    print(response['MetricAlarms'])