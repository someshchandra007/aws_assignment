import json
import boto3

# create ssm and s3 clients
ssm = boto3.client('ssm')
s3 = boto3.resource('s3')

# function to get value for a key and write in S3
def lambda_handler(event, context):
    # TODO implement
    parameter = ssm.get_parameter(Name='UserName',WithDecryption=True)
    keyvalue=parameter['Parameter']['Value']
    data_set = {"UserName" : keyvalue}
    returndata = json.dumps(data_set)
    #print(returndata)
    obj = s3.Object('app-input-data','param.json')
    obj.put(Body=json.dumps(data_set))
    
    return {
        'statusCode': 200,
        'body': returndata
    }
