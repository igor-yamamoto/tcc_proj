import json

allowed_devices_guid = [
    "001"
]

def validate_json(message):
    try:
        message = json.loads(message)
        return message, 0
    except:
        print(f"Message '{message}' coudn't be serialized as json object.")
        return '', 400

def main(message):
    message, status = validate_json(message)

    if status == 0:
        try:
            context = message['context']
        except: 
            print(f"Coudn't extract context from from message '{message}'. Returning 'dump' string.")
            context = 'dump'
        message = json.dumps(message)
        
# message = json.dumps(message)
        return message, context