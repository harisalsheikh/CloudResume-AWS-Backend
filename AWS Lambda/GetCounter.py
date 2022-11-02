import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    
    client = boto3.resource("dynamodb")
    table = client.Table("CloudResumeChallenge")
    
    # Get all items 
    scan_table = table.scan()["Items"]
    
    # Get Counter Item from table
    
    #empty list to store content of the "Counter" Item
    item = []
    
    for items in scan_table:
        item.append(items["Counter"])
        
    return item