import os
cmd = ['sensuctl asset create sensu-plugins-load-checks --url "https://assets.bonsai.sensu.io/1accacdd780175a02183e722effa0986e6472f21/sensu-plugins-load-checks_5.0.0_debian_linux_amd64.tar.gz" --sha512 "3e171c28e6bdaecc7d164fa4c49dea193e95508609436866bc973b14ce49a0d07ce5314a78010490f954790d9194260cc59344e2a0c0fec74ae856973674dd66"',
       "sensuctl check create check-load \
        --command 'check-load.rb -c 2,200,200 -w 1,100,100' \
        --interval 60 \
        --subscriptions system \
        --runtime-assets sensu-plugins-load-checks,sensu-ruby-runtime", "sudo service sensu-agent restart", 'sensuctl asset list', 'sudo service sensu-agent restart']
for i in range(len(cmd)):
    os.system(cmd[i])
    print("{} is compleated...................".format(cmd[i]))

print("Check-load alert is created..........")
os.system("sensuctl event list")