import os
cmd = ['sensuctl asset create sensu-plugins-memory-checks --url "https://assets.bonsai.sensu.io/c5391d4ae186484226732344b35cf95c0b07b8ec/sensu-plugins-memory-checks_4.0.0_debian_linux_amd64.tar.gz" --sha512 "3c61ab6f4eb5dea4ee816e4f9a4f857660ac32648d0ecd7804e1827351d8fe021f29e557d9600ecac8cd16d261c8ff2dc113790a544ce1148a8cb321546552d6"',
       "sensuctl check create check-memory \
        --command 'check-memory-percent.rb -w 70 -c 80' \
        --interval 60 \
        --subscriptions system \
        --runtime-assets sensu-plugins-memory-checks,sensu-ruby-runtime", "sudo service sensu-agent restart", 'sensuctl asset list', 'sudo service sensu-agent restart']
for i in range(len(cmd)):
    print("--------{} is started -----------".format(cmd[i]))
    os.system(cmd[i])
    print("--------{} is compleated -----------".format(cmd[i]))
print("Check-memory alert is created..........")
os.system("sensuctl event list")