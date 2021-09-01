import subprocess
import platform

def doPing(ip):
    parameter = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', parameter, '1', ip]
    return subprocess.check_output(command)