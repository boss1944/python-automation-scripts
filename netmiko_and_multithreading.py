from netmiko import ConnectHandler
from datetime import datetime
import time
import threading
start = time.time()

# define the commands that will be run on all devices
# by all the threads
def backup(cisco_device):
    connection = ConnectHandler(**cisco_device)
    print('Entering enable mode...')
    connection.enable()

    output = connection.send_command('show run')
    prompt = connection.find_prompt()
    hostname = prompt[0:-1]

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    # save the device configuration file from each device
    filename = f'{hostname}_{year}_{month}_{day}_backup.txt'
    with open(filename, 'w') as backup:
        backup.write(output)
        print(f'Backup of {hostname} completed successfully')
        print('#' * 30)

    print('Closing connection')
    connection.disconnect()

# open the text file containing the device
# ip addresses and read each line
with open('devices.txt') as f:
    devices = f.read().splitlines()

# create a list containing the threads
threads = list()

# iterate over the ip addresses, add each one to 
# to the 'host' key in the dictionary, connect
# to each device in turn and perform the backup
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
    th = threading.Thread(target=backup, args=(cisco_device,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join

end = time.time()
print(f'Total execution time: {end-start}')