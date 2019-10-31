#coreditor by ArSiFoX. Version:1.1
def connect():
	print("Connecting...")
	print("0%")
	print("15%")
	print("75%")
	print("100%")
while True:
	cmd = input("Enter a command >")
	if cmd == "connect":
		n = input("Enter IP address: ")
		connect()
		print("Connected to "+n)
	else:
		if cmd == "trace":
			y = input("Enter port: ")
			t = " has been traced"
			print("Port "+y+t)
		else:
				if cmd == "unconnect":
					a = input("Enter ip: ")
					print("unconnected from "+a)
				else:
					if cmd == "stop":
						break
					else:
						if cmd == "stress":
							stress = input("Enter ip: ")
							print("IP "+stress, "has been stressed!")
						else:
								if cmd == "breakhost":
									ip1 = input("Enter ip: ")
									print("host "+ip1, "has been broked!")
								else:
									print("Command not finded!")