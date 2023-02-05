import subprocess

def connect_to_wifi(ssid, password):
    cmd = "sudo iwconfig wlan0 essid '{}' key s:{}".format(ssid, password)
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

ssid = "YourNetworkSSID"
password = "YourNetworkPassword"
connect_to_wifi(ssid, password)
