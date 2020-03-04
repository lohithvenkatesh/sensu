import os
cmd = ['sudo apt-get update', 'sudo apt-get upgrade -y', 'curl -s https://packagecloud.io/install/repositories/sensu/stable/script.deb.sh | sudo bash',
       'sudo apt-get install sensu-go-backend','sudo curl -L https://docs.sensu.io/sensu-go/latest/files/backend.yml -o /etc/sensu/backend.yml',
       'sudo service sensu-backend start', "curl -s https://packagecloud.io/install/repositories/sensu/stable/script.deb.sh | sudo bash",
       "sudo apt-get install sensu-go-cli",
       "sensuctl configure -n \
        --username 'admin' \
        --password 'P@ssw0rd!' \
        --namespace default \
        --url 'http://127.0.0.1:8080'",
       'curl http://127.0.0.1:8080/health']
for i in range(len(cmd)):
    print("--------{} is started -----------".format(cmd[i]))
    os.system(cmd[i])
    print("--------{} is compleated -----------".format(cmd[i]))

print("open:http://localhost:3000 use user name:admin and password:P@ssw0rd! to log in into ")