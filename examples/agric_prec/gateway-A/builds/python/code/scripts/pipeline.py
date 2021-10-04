import json

import devices_info

def allowed_devices_list():
    temperature_devices = list(devices_info.temperature_devices.keys())
    humidity_devices = list(devices_info.humidity_devices.keys())
    luminosity_devices = list(devices_info.luminosity_devices.keys())
    ph_devices = list(devices_info.ph_devices.keys())

    allowed_guids = {}

    for device in temperature_devices:
        allowed_guids[device] = 'temperature'
    for device in humidity_devices:
        allowed_guids[device] = 'humidity'
    for device in luminosity_devices:
        allowed_guids[device] = 'luminosity'
    for device in ph_devices:
        allowed_guids[device] = 'ph'

    return allowed_guids
    
allowed_devices_guid_context = allowed_devices_list()
allowed_devices_guid = list(allowed_devices_guid_context.keys())

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
        context = allowed_devices_guid_context[message['device_guid']]

        if status == 0:
            message = json.dumps(message)

    # message = json.dumps(message)
            return message, context