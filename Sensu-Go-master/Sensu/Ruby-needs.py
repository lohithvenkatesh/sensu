import os
cmd = ['apt install ruby-dev libffi-dev build-essential',
'gem install text-table & gem install sensu-plugin','sudo apt-get install ruby-full','sudo apt-get install rubygems build-essential',
'sudo apt-get install rubygems']
for i in range(len(cmd)):
    os.system(cmd[i])
    print("{} is compleated".format(cmd[i]))
print("Ruby needs installed successfully..........")
os.system("ruby -v")