import json,boto3,time,base64,botocore.response as br
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime, timedelta
dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

def lambda_handler(event, context):
    print(event)
    yesterday_date_time = str(datetime.now() - timedelta(days = 1))
    
    table_event = dynamodb.Table('poc-rpp-event-tracking')
    response_scans = table_event.query(
        KeyConditionExpression=Key('event_type').eq('qr_scan') & Key('timestamp').gt(yesterday_date_time)
    )
    response_payments = table_event.query(
        KeyConditionExpression=Key('event_type').eq('payment') & Key('timestamp').gt(yesterday_date_time)
    )

    num_successful_payments=response_payments['Count']
    num_qrs_scanned=response_scans['Count']
    
    num_to_send = 15
    
    index = -1
    response_users = []
    members = []
    while abs(index) <= num_qrs_scanned and num_to_send >= 0:
        if not response_scans['Items'][index]['member_id'] in response_users:
            response_users.append(response_scans['Items'][index]['member_id'])
            members.append(response_scans['Items'][index])
            num_to_send -= 1
        index -= 1
        
    # Construct response to UI from the different pieces assembled
    response_dict = {}
    response_dict['num_successful_payments'] = num_successful_payments
    response_dict['num_qrs_scanned'] = len(members)
    response_dict['latest_member_scans'] = members
    if 'verify_results' in event.keys():
        response_dict['verify_results'] = event['verify_results']
    
    # If the function was called by qr scan, send the update to all active connections
    if event:
        # Get the connection id of all connected clients and push the update to them
        table_connections = dynamodb.Table('poc-rpp-websocket-connections')
        
        response_connections = table_connections.scan()
        
        for item in response_connections['Items']:
            connectionId = item['connectionid']
            try:
                #Use a layer or deployment package to 
                #include the latest boto3 version.
                apiManagement = boto3.client('apigatewaymanagementapi', region_name='us-east-1',
                                      endpoint_url='https://4ifv0gvm0j.execute-api.us-east-1.amazonaws.com/dev/')
                connection_status = apiManagement.get_connection(ConnectionId=connectionId)
                
                print(connection_status)
                response = apiManagement.post_to_connection(Data=json.dumps(response_dict),ConnectionId=connectionId)
            except:
                response = table_connections.delete_item(
                    Key={
                        'connectionid': connectionId
                    }
                )
        
    return {
        'statusCode': 200,
        'body': json.dumps(response_dict)
    }
