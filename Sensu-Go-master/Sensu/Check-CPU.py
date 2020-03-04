import os
cmd = ['sensuctl asset create sensu-plugins-cpu-checks --url "https://assets.bonsai.sensu.io/68546e739d96fd695655b77b35b5aabfbabeb056/sensu-plugins-cpu-checks_4.0.0_debian_linux_amd64.tar.gz" --sha512 "da5a183ad1a1f76962561eed659c6184b3e5d6a412432e1ccb4297cce123c41f9a8bb4fdb9ab19663aada978ea862ab2bd5f00bc91e4769ddd87543f5662b3af"',
       'sensuctl asset create sensu-ruby-runtime --url "https://assets.bonsai.sensu.io/5123017d3dadf2067fa90fc28275b92e9b586885/sensu-ruby-runtime_0.0.10_ruby-2.4.4_debian_linux_amd64.tar.gz" --sha512 "a28952fd93fc63db1f8988c7bc40b0ad815eb9f35ef7317d6caf5d77ecfbfd824a9db54184400aa0c81c29b34cb48c7e8c6e3f17891aaf84cafa3c134266a61a"',
       'sensuctl asset list', "sensuctl check create check-cpu \
        --command 'check-cpu.rb -w 75 -c 90' \
        --interval 60 \
        --subscriptions system \
        --runtime-assets sensu-plugins-cpu-checks,sensu-ruby-runtime", "sudo service sensu-agent restart"]
for i in range(len(cmd)):
    os.system(cmd[i])
    print("{} is compleated".format(cmd[i]))
print("CPU-check is created successfully..........")
os.system("sensuctl event list")
