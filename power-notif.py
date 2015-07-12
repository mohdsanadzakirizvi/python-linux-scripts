from time import sleep
import pynotify
def notify(title,body):
	pynotify.init('test')
	n=pynotify.Notification(title,body)
	n.show()
def status():
	power_file=open("/sys/class/power_supply/BAT0/capacity","r")
	power= int(power_file.readline())
	if power >=90:
		notify("Stop Charging !! \n", "battery is:%d %%" %(power))
	elif power<=30:
 		notify("CHARGE!! YOUR BATTERY IS  LOW! \n","battery is:%d %%" %(power))
	sleep(600)#check after every ten minutes
	status()
def main():
	res = raw_input("Do you wish to start? Enter 1 for yes 0 for no\n ")
	if res:
		status()
	else :
		exit()
if __name__ == '__main__':
    main()
