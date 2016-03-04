import sys
import subprocess

def exitting():
	print("[-] Exiting")
	sys.exit()

def script():
	cmd1_output = subprocess.check_output("netsh wlan show drivers", shell=True)
	if "Hosted network supported  : Yes" in cmd1_output:
		print("[+] Driver supported")
	hot_name = raw_input("Name for your hotspot: ")
	password = raw_input("Enter your password (include alphanumeric): ")
	while(len(password)<8):
		print("\n[-] Insufficient password strength. Try again ")
		password = raw_input("Enter your password (include alphanumeric): ")
	cmd2 = "netsh wlan set hostednetwork mode=allow ssid="+hot_name+" key="+password
	cmd2_output = subprocess.check_output(cmd2, shell=True)
	if "successfully changed" in cmd2_output:
		print("[+] Hotspot created")
		cmd3_output = subprocess.check_output("netsh wlan start hostednetwork", shell=True)
		if "started" in cmd3_output:
			print("[+] The hotspot is up and running")
		else:
			print("[-] Oops, Something went wrong")
			exitting()
#		stat = "a"
#		while (stat != "q"):
		stat = raw_input("\nPress any key to stop hotspot ")
		cmd4_output = subprocess.check_output("netsh wlan stop hostednetwork", shell=True)
		print("\n[+] Hotspot has been stopped")
		print("[+] Thanks for using")
		print("[+] For details contact @bnchandrapal")


def Main():
	print ("[+] Checking for admin status")
	try:
		output = subprocess.check_output("whoami /groups | find \"S-1-16-12288\"", shell=True)
	except:
		print("[-] You are not admin :( ")
		exitting()
	if('S-1-16-12288' in output):
		print("[+] The program is running with Admin priv :)")
		print("[+] Initiating the script")
		script()
		
if __name__ == '__main__':
	Main()