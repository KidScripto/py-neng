'''
Authored:
Referenced work: FastAPI course
Date:
'''

import subprocess
import argparse

#Argument Definition
parser = argparse.ArgumentParser(description="Define IP address, ping count")
parser.add_argument('-i', '--ipAddr', help='Target IP address', type=str, required=True)
parser.add_argument('-c', '--count', help='Count number', type=int, required=True)
args = parser.parse_args()


def ping_ip():
    reply = subprocess.run(['ping', '-c', str(args.count), '-n', str(args.ipAddr)],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    
    if reply.returncode == 0:
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    ping_ip()
