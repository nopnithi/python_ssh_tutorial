from paramiko import SSHClient, AutoAddPolicy
from time import sleep
from re import match


def get_output(session):
    return session.recv(65535).decode('utf-8').rstrip()


def find_prompt(output):
    last_line = output.splitlines()[-1].strip()
    if match(r'([\w-]+)(>|(?:\(config.*\))*#)', last_line):
        return True
    return False


def send_command(session, command):
    cmd_output = ''
    session.send(command + '\n')
    sleep(0.3)
    while True:
        _output = get_output(session)
        cmd_output += _output
        if find_prompt(_output):
            break
    return cmd_output


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
        _output = get_output(session)
        output += _output
        if find_prompt(_output):
            cmd_output = send_command(session, 'terminal length 0')
            output += cmd_output
            cmd_output = send_command(session, 'show running-config')
            output += cmd_output
            print(output.strip())


if __name__ == '__main__':
    main()
