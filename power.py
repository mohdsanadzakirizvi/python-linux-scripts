from time import sleep
def status():
    sleep(10)
    power_file=open("/sys/class/power_supply/BAT0/capacity","r")
    print power_file.readline()
    status()
val = raw_input("Do you want to start? enter 1 for yes 0 for no")
if val:
    status()
