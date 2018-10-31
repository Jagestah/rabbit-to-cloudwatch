import requests
from requests.compat import urljoin
from requests.auth import HTTPBasicAuth
import boto3
import os
from utils.logging import logger as log

client = boto3.client('cloudwatch', region_name='us-east-1')

URL = os.environ['RABBIT_MQ_URL']
USERNAME = os.environ['RABBIT_MQ_USERNAME']
PASSWORD = os.environ['RABBIT_MQ_PASSWORD']

requestURL = URL+'/api/queues'
#print('requestURL='+requestURL)

def put_metric(metrics):
    client.put_metric_data(
        Namespace='Resource/RabbitMQ',
        MetricData=metrics
    )


if __name__ == '__main__':
    total_messages = 0
    resp = requests.get(requestURL, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    #print(resp)
    if resp.status_code == 200:
        queues = resp.json()
        count = 0
        metrics = []
        for q in queues:
            if q['name'].endswith('activity.created'):
                messages = q['messages']
                name = q['name']
                #print(name)
                count = count + 1
                # if count % 10 == 0:

                metrics.append({
                        'MetricName': name,
                        'Dimensions': [
                            {
                                'Name': 'Resource',
                                'Value': 'RabbitMQ'
                            },
                        ],
                        'Value': messages,
                        'Unit': 'Count',
                        'StorageResolution': 60
                    })
                try:
                    put_metric(metrics)
                    metrics = []
                    count = 0
                    print('put metric ' +name)
                except:
                    print('unable to put metric '+name)
                    pass
        # if len(metrics) > 0:
        #   put_metric(metrics)
        # log.info("Total messages: %s", total_messages)
    else:
        log.error('error', resp.status_code)
