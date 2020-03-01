from netmiko import ConnectHandler

cisco_asa = {
    'device_type': 'cisco_asa',
    'host':   '192.168.1.245',
    'username': 'Taylor',
    'password': '159753Pfhs',
    'port' : 22,          # optional, defaults to 22
    'secret': 'cisco123',     # optional, defaults to ''
}

net_connect = ConnectHandler(**cisco_asa)

output = net_connect.send_command('show int ip brief')

net_connect.disconnect()

print(output)

with open('Show_interface.txt','w') as f:
    f.write(output)

