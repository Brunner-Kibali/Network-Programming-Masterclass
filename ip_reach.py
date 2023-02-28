import sys
import subprocess

# Checking IP reachability
def ip_reach(list):
    for ip in list:
        ip = ip.lstrip(" ").rstrip("\n")
        # subprocess module used to execute ping with 2 echo requests/packets
        # DEVNULL is used to suppress the output of messages/ping errors
        ping_reply = subprocess.call("ping %s -c 2" % (ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

        if ping_reply == 0:
            print("\n* {} is reachable :) \n".format(ip))
            # Test the reachability of the next IP in the list
            continue

        else:
            print("\n {} not reachable :( Check connectivity and try again.".format(ip))
            sys.exit()
