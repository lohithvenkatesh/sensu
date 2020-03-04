import os
li = ['git clone https://github.com/sagarreddyg/Sensu-checks.git','mv Sensu-checks/check-load.rb /home/ubuntu/check-load.rb','cd /home/ubuntu/', 'chmod +x check-load.rb',
      "sensuctl check create check-load --command '/home/ubuntu/check-load.rb -c 4,100,100 -w 3,3,3' --interval 60 --subscriptions system --runtime-assets sensu-ruby-runtime"]
for i in range(len(li)):
    print("--------{} is started -----------".format(li[i]))
    os.system(li[i])
    print("--------{} is compleated -----------".format(li[i]))
os.system("sensuctl check list")
