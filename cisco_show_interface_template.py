from netmiko import ConnectHandler

cisco_asa = {
    'device_type': 'cisco_asa',
    'host':   '192.168.1.1',
    'username': ',user',
    'password': 'password',
    'port' : 22,          # optional, defaults to 22
    'secret': 'cisco',     # optional, defaults to ''
}

net_connect = ConnectHandler(**cisco_asa)

output = net_connect.send_command('show int ip brief')

net_connect.disconnect()

print(output)

with open('Show_interface.txt','w') as f:
    f.write(output)

