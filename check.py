from scrapli.driver.core import IOSXEDriver
MY_DEVICE = {
	"host": "devnetsandboxiosxe.cisco.com",
	"auth_username": "admin",
	"auth_password": "C1sco12345",
	"auth_strict_key": False,
	"transport": "paramiko"

}

conn = IOSXEDriver(**MY_DEVICE)
conn.open()
commands = [
	"show ip interface brief",
	"show ip route",
	"show ip arp",
	"show version",
	"show vlan brief",
	"show interfaces"
]
for command in commands:
	response = conn.send_command(command)
	print(response.result)
conn.close()
