from time import sleep


def status():
    battery_percent = open("/sys/class/power_supply/BAT0/capacity", "r")
    charging_status = open("/sys/class/power_supply/BAT0/status", "r")
    print "BATTERY :%s%%" % (battery_percent.read()), "\nSTATUS : %s" % (charging_status.readline())
    sleep(10)
    status()
val = raw_input("Do you want to start? enter 1 for yes 0 for no\n")
if val:
    status()
