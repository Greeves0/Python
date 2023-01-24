import network

# user data
ssid = "Lfpddotdoyclgcot073969195dysu3" # wifi router name
pw = "CmaBite!" # wifi router password

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, pw)

# wait for connection
while not wifi.isconnected():
    pass

# wifi connected
print(wifi.ifconfig())