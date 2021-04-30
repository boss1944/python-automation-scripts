from netmiko import ConnectHandler

# open the text file containing the device ip
# addresses and read each line into a list
with open('devices.txt') as f:
    devices = f.read().splitlines()

# create and empty list of devices
device_list = list()

# iterate over the ip addresses, add each one to 
# to the 'host' key in the dictionary and append
# all dictionaries to the list
for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'admin',
        'password': 'Cisco12',
        'port': 22,          
        'secret': 'Cisco12', 
        'verbose': True      
    }
    device_list.append(cisco_device)

# connect to each device in turn, prompt the user for a configuration file and run
# the commands from the file on each device
for device in device_list:
    connection = ConnectHandler(**device)

    print('Entering enable mode...')
    connection.enable()

    file = input(f'Enter a configuration file (use valid path) for {device["host"]}:')

    print(f'Running commands from file: {file} on device: {device["host"]}')
    output = connection.send_config_from_file(file)
    print(output)

    print(f'Closing connection to {device["host"]}')
    connection.disconnect()

    print('#' * 30)