## To find out what all processes are running and which ports are open on a server

import os


def get_nmap(options, ip):
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
