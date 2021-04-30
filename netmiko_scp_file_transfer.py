from netmiko import ConnectHandler
from netmiko import file_transfer

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.137.20',
    'username': 'admin',
    'password': 'Cisco12',
    'secret': 'Cisco12',
    'verbose': True
}

connection = ConnectHandler(**cisco_device)

# define the SCP parameters
transfer_output = file_transfer(connection, source_file='running-config.txt', 
                                dest_file='startup-config', file_system='nvram:',
                                direction='put', overwrite_file=True)

# confirm the transfer has completed
print(transfer_output)

connection.disconnect()