import boto3
import json


session = boto3.session.Session(profile_name='dev_admin')
# Create SQS client
sqs = session.client('sqs')

queue_url = 'https://sqs.us-west-2.amazonaws.com/714767054201/testRajesh.fifo'

for event_name,message_group_id in [("memberPermissionReset", "200016656552"), ("DCM_partyPermission", "200016656552")]:
    for x in range(1):
        message_attributes = {
            'Author': {
                'DataType': 'String',
                'StringValue': 'Rajesh Kaushik'
            }
        }
        message = {
            "action": "update",
            "systemLocale": "bright",
            "documentType": "member",
            "eventName": event_name,
            "sourceDocumentName":message_group_id,
            "payload": {
                "officeKey": "200016656552",
                "dedup_counter": f'{x}'
            }
        }
        # Send message to SQS queue
        response = sqs.send_message(
            QueueUrl=queue_url,
            #DelaySeconds=10,
            #MessageDeduplicationId='string',
            MessageGroupId=message_group_id,
            MessageAttributes=message_attributes,
            MessageBody=json.dumps(message)
        )

        print(response['MessageId'])
