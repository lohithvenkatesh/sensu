import requests
import boto3
import sys

region = requests.get("http://169.254.169.254/latest/dynamic/instance-identity/document").json()['region']
client = boto3.client('elbv2', region_name = region)
tgs = client.describe_target_groups()["TargetGroups"]
unhealthy = 0
for tg in tgs:
    if tg["TargetGroupName"] in ["sg-userservice-i", "sg-commservice-i", "sg-feedservice-i", "sg-catalogservice-i", "sg-schedulerservice-i", "sg-orderrules-i", "sg-ruleservice-i", "sg-cartservice-i","sg-navapp","sg-catalog"]:
      continue
    tgHealthDescriptions = client.describe_target_health(TargetGroupArn=tg["TargetGroupArn"])["TargetHealthDescriptions"]
    for t in tgHealthDescriptions:
        if t["TargetHealth"]["State"] != "healthy":
            unhealthy += 1
            print("{0} {1} in {2}".format(t["Target"]["Id"], t["TargetHealth"]["State"], tg["TargetGroupName"]))

if unhealthy > 0:
    print("{} unhealthy hosts found".format(unhealthy))
    sys.exit(2)
