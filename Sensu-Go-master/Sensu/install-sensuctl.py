import os
cmd =["curl -s https://packagecloud.io/install/repositories/sensu/stable/script.deb.sh | sudo bash", "sudo apt-get install sensu-go-cli",
      "sensuctl configure -n \
--username 'admin' \
--password 'P@ssw0rd!' \
--namespace default \
--url 'http://127.0.0.1:8080'", "sensuctl config view"]
for i in range(len(cmd)):
    os.system(cmd[i])
    print("{} is compleated".format(cmd[i]))
print("sensuctl is installed successfully............")
