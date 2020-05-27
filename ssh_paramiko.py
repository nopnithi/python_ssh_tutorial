from paramiko import SSHClient, AutoAddPolicy
from time import sleep


with SSHClient() as client:
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(
        hostname='10.1.30.101',
        username='nopnithi',
        password='P@ssw0rd',
        look_for_keys=False
    )
    session = client.invoke_shell()
    session.send('show version | include uptime' + '\n')
    sleep(1)
    output = session.recv(32768).decode('utf-8')
    print(output.strip())
