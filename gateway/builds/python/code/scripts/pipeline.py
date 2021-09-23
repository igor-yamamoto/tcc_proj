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

def allowed_devices(message):
    try:
        device_guid = message['device_guid']
        if device_guid in allowed_devices_guid:
            return message, 0
        else:
            print(f"Device with guid '{device_guid}' not set as allowed.")
            return '', 400
    except:
        print(f"Field 'device_guid' not configured. Ignoring")
        return '', 400

def main(message):
    message, status = validate_json(message)

    if status == 0:
        message, status = allowed_devices(message)

    message = json.dumps(message)

    return message