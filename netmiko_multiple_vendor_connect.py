from netmiko import ConnectHandler

# set up the connection credentials for each device
cisco_router = {
    'device_type': 'cisco_ios',
    'ip': '192.168.137.20',
    'username': 'admin',
    'password': 'Cisco12',
    'secret': 'Cisco12',
    'verbose': True
}

cisco_switch = {
    'device_type': 'cisco_ios',
    'ip': '192.168.137.30',
    'username': 'admin',
    'password': 'Cisco12',
    'secret': 'Cisco12',
    'verbose': True
}

juniper_router = {
    'device_type': 'juniper_junos',
    'ip': '192.168.137.10',
    'username': 'admin',
    'password': 'Junos123',
    'verbose': True
}
# create a list of the devices 
devices = [cisco_router, cisco_switch, juniper_router]

# iterate over the list of devices and display the device
# cli prompt and device type
def main():
    for device in devices:
        device_connect = ConnectHandler(**device)
        output = device_connect.find_prompt()
        print('\n' + '#' * 80)
        print(f"\n-------- Device {device['device_type']}--------")
        print(output)
        print('\n' + '#' * 80)
        print('Closing connection' + '\n')
        device_connect.disconnect()

if __name__ == '__main__':
    main()
