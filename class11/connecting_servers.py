import paramiko



client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# linux
client.load_system_host_keys()
client.connect('192.168.33.10')

# # windows
# client.connect('192.168.33.10', username="root", key_filename="id_rsa")

stdin, stdout, stderr = client.exec_command('ls -l')

k = stdout.readlines()
client.close()
print(k)
