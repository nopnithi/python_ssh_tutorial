from paramiko import SSHClient, AutoAddPolicy
from time import sleep
from re import match


def find_prompt(output):
    last_line = output.splitlines()[-1].strip()
    if match(r'([\w-]+)(>|(?:\(config.*\))*#)', last_line):
        return True
    return False


def main():
    output = ''
    with SSHClient() as client:
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(
            hostname='10.1.30.101',
            username='nopnithi',
            password='P@ssw0rd',
            look_for_keys=False
        )
        session = client.invoke_shell()
        _output = session.recv(65535).decode('utf-8').rstrip()
        output += _output
        if find_prompt(_output):
            print('Got prompt, login is successful')
            session.send('show version | include uptime' + '\n')
            sleep(1)
            _output = session.recv(65535).decode('utf-8').rstrip()
            output += _output
            if find_prompt(_output):
                print('Got prompt, sending command is successful')
                print(output.strip())


if __name__ == '__main__':
    main()
