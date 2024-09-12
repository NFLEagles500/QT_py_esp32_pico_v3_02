# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl

import network
import hostname
import envSecrets

def do_connect():
    import network
    
    wlan = network.WLAN(network.STA_IF)
    network.hostname(hostname.hostname)
    print(network.hostname())
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(envSecrets.ssid, envSecrets.wifipsw)
        while not wlan.isconnected():
            pass
    #print('network config:', wlan.ipconfig('addr4'))
do_connect()
print('connected')
#webrepl.start()
