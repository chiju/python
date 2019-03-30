from datetime import datetime, timedelta
import subprocess
import re
import sys

after_1mins = datetime.now() + timedelta(minutes=1)

servers = ["54.152.9.243", "34.238.39.221", "54.89.215.120"]

def process_sdkms():
    if after_1mins > datetime.now():        
        for server in servers:
            command = ["ssh", "-i", "/Users/chiju/terra", "ubuntu@" + server, 'sudo', 'ps', '-A', '|', 'grep', 'nginx', '|', 'awk', "-F'", "'", "'{print", "$1}'", '|', 'head', '-1']            
            sdkms_pid = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True).stdout
            if re.match("[0-9]+", sdkms_pid):
                print("{} <=====> {}".format(server, sdkms_pid))
                servers.remove(server)
                if len(servers) == 1:
                    process_sdkms()
            else:
                process_sdkms()
    else:
        print("1 minutes over")
        quit()
process_sdkms()
