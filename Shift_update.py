import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
import ast

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ShiftDetails')

def lambda_handler(event, context):
    parsed_json=eval(str(event))
    print(parsed_json)
    start_datetime=parsed_json['result']['shifts'][0]['start_time']
    end_datetime=parsed_json['result']['shifts'][0]['end_time']
    start_date=start_datetime[:10]
    end_date=end_datetime[:10]
    start_time=start_datetime[-9:].strip()
    end_time=end_datetime[-9:].strip()
    primary_contact=parsed_json['result']['shifts'][0]['primary']['contact_number']
    primary_name=parsed_json['result']['shifts'][0]['primary']['name']
    secondary_contact=parsed_json['result']['shifts'][0]['secondary']['contact_number']
    secondary_name=parsed_json['result']['shifts'][0]['secondary']['name']
    tertiary_contact=parsed_json['result']['shifts'][0]['tertiary']['contact_number']
    tertiary_name=parsed_json['result']['shifts'][0]['tertiary']['name']
    
    #tertiary_json=json.dumps(tertiary_json)
    jsons=['primary_json','secondary_json','tertiary_json']
    table.put_item(
        Item={"Name":primary_name,
    "Contact_Number":primary_contact,
    "Start_Date":start_date,
    "Start_Time":start_time,
    "End_Date":end_date,
    "End_Time":end_time})
        table.put_item(
        Item={"Name":secondary_name,
    "Contact_Number":secondary_contact,
    "Start_Date":start_date,
    "Start_Time":start_time,
    "End_Date":end_date,
    "End_Time":end_time})
        table.put_item(
        Item={"Name":tertiary_name,
    "Contact_Number":tertiary_contact,
    "Start_Date":start_date,
    "Start_Time":start_time,
    "End_Date":end_date,
    "End_Time":end_time})
