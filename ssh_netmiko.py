from netmiko import ConnectHandler

device = {
    'host': '10.1.30.101',
    'username': 'nopnithi',
    'password': 'P@ssw0rd',
    'secret': 'P@ssw0rd',
    'device_type': 'cisco_ios',
    'fast_cli': True
}
with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command('show version | include uptime')
    print(output.strip())
