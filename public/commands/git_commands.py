import subprocess as sb
import yaml


# read variable from yaml file
# it should not be like php/project_root/kubernetes/config.yaml. suppose 
# it is runn from apply.py directory 
with open("../../php/project_root/kubernetes/config.yaml", "r") as t:
    data = yaml.safe_load(t)
    tag = data["data"]["IMAGE_TAG"]

commands = [
    # testing
    "git add .",
    f'git commit -m "Current application version: {tag}"',
    "git push",

]
for command in commands:
    try:
        sb.run(command, check=True, shell=True)
        print(f"The command {command} exected successfully \n")
        print("----------------Command------------------------")
    except sb.CalledProcessError as e:
        print(f"The error is {e}")
