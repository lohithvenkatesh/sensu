import boto.ec2
import datetime
import dateutil
import sys
from dateutil import parser
#import smtplib
#from email.MIMEMultipart import MIMEMultipart
#from email.MIMEText import MIMEText
import json, ast

region='asia pacific'
m=0

instances_ids = []

#Verifying role tag of instances
conn=boto.ec2.connect_to_region(region,validate_certs=False)
reservations = conn.get_all_instances(filters={"tag:require_snapshot" : "yes*"})
instances = [i for r in reservations for i in r.instances]
for i in instances:
       #print "%s"% i.id
        instances_ids.append(i.id)
print(ast.literal_eval(json.dumps(instances_ids)))


#Verify volume tags
mysql_volumes=[]
reservations = conn.get_all_instances(filters={"tag:require_snapshot" : "yes*"})
instances = [i for r in reservations for i in r.instances]
for i in instances:
#       print i.id
        volumes=conn.get_all_volumes(filters={'attachment.instance-id': i.id,"tag:Mountpoint" : "/var/lib/mysql*"})
#       print volumes
        if not volumes:
                print('Untagged volumes for the instance %s \n'% i.id)
                #sys.exit(2)
#                log_write('Untagged volumes for the instance %s \n'% i.id)
                m+=1
        for volume in volumes:
                mysql_volumes.append(volume.id)
                print(ast.literal_eval(json.dumps(mysql_volumes)))

#Verify latest db snapshots(1 day)
latest_snapshots = []
for v in mysql_volumes:
#snapshot=conn.get_all_snapshots(filters={'volume-id':v})[0]# If not even one snapshot available, script will break here.
        list_of_snaps = []
        snapshots=conn.get_all_snapshots(filters={'volume-id':v})
        if  snapshots:
                #print snapshots
                for snap in (conn.get_all_snapshots(filters={'volume-id':v})):
                        list_of_snaps.append({'date':snap.start_time, 'snap_id': snap.id})
                new_snapshot=sorted(list_of_snaps, key=lambda k: k['date'], reverse=True)[0]['snap_id']
                new_snapshot_time=sorted(list_of_snaps, key=lambda k: k['date'], reverse=True)[0]['date']
                timeLimit=datetime.datetime.now() - datetime.timedelta(days=1)
                if parser.parse(new_snapshot_time).date() >= timeLimit.date():
#                               print new_snapshot
                                latest_snapshots.append(new_snapshot)
                else:
                                print("Snapshot missing for volume %s"% v)
                                #sys.exit(2)
                               # log_write("Snapshot missing for db volume %s"% v)
                                m+=1
print(set(latest_snapshots))
if m > 0:
    sys.exit(2)
else:
    sys.exit(0)
