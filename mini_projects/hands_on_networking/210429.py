from netmiko import ConnectHandler
import jnpr.junos

r2 = {'device_type': 'cisco_ios', 'host': '121.74.1.4', 'username': 'admin', 'password': 'admin123', 'port': '2022'}  

r2_facts = r2.get_facts
net_connect_r2 = ConnectHandler(**r2)
result = net_connect_r2.send_command("show ip interface brief", use_textfsm=True)
# Send a command to the router
output = net_connect_r2.send_command("show ipv4 interface brief")
print(output)