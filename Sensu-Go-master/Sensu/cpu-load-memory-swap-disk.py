import checks.check as ck
import os
cmd = [ck.CPU(), ck.DISK(), ck.Load(), ck.Memory(), ck.Swap()]
for x in cmd:
    for i in range(len(x)):
        print("--------{} is started -----------".format(cmd[i]))
        os.system(x[i])
        print("-------------{} is compleated ------------".format(cmd[i]))
os.system("sudo service sensu-agent restart & sensuctl asset list & sensuctl check list")