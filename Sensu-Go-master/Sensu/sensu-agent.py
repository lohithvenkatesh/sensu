import os
cmd = ["sudo apt-get update",'curl -s https://packagecloud.io/install/repositories/sensu/stable/script.deb.sh | sudo bash', 'sudo apt-get install sensu-go-agent',
       'sudo curl -L https://docs.sensu.io/sensu-go/latest/files/agent.yml -o /etc/sensu/agent.yml',
       'service sensu-agent start', 'sensuctl asset create sensu-ruby-runtime '
                                    '--url "https://assets.bonsai.sensu.io/5123017d3dadf2067fa90fc28275b92e9b586885/sensu-ruby-runtime_0.0.10_ruby-2.4.4_debian_linux_amd64.tar.gz" '
                                    '--sha512 "a28952fd93fc63db1f8988c7bc40b0ad815eb9f35ef7317d6caf5d77ecfbfd824a9db54184400aa0c81c29b34cb48c7e8c6e3f17891aaf84cafa3c134266a61a"']
for i in range(len(cmd)):
    print("--------{} is started -----------".format(cmd[i]))
    os.system(cmd[i])
    print("--------{} is compleated -----------".format(cmd[i]))
print("Sensu-agent is installed success fully......")
os.system("sensu-agent version")