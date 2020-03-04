import os
cmd = ['sensuctl asset create sensu-plugins-disk-checks --url "https://assets.bonsai.sensu.io/73a6f8b6f56672630d83ec21676f9a6251094475/sensu-plugins-disk-checks_5.0.0_debian_linux_amd64.tar.gz" --sha512 "efcc00a70ed8ebcab401b7dbd595d770a2b441e56d99143a923cbfc98977f6d085388b7411da706d47e6150b31ffa9b41ba78a0ee35a0e19eb21eee713009e19"',
       "sensuctl check create check-disk \
        --command 'check-disk-usage.rb -w 75 -c 90 -p /snap' \
        --interval 60 \
        --subscriptions system \
        --runtime-assets sensu-plugins-disk-checks,sensu-ruby-runtime", "sudo service sensu-agent restart", 'sensuctl asset list', 'sudo service sensu-agent restart']
for i in range(len(cmd)):
    print("--------{} is started -----------".format(cmd[i]))
    os.system(cmd[i])
    print("-------------{} is compleated ------------".format(cmd[i]))

print("Check-disk alert is created..........")
os.system("sensuctl event list")
