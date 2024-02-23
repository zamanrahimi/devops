import subprocess as sb
import yaml

# get absolute git_command.py path

import os
# Get the absolute path to the current script
script_directory = os.path.dirname(os.path.abspath(__file__))
# Construct the relative path to the yaml file
yaml_file_path = os.path.join(script_directory, "../../php/project_root/kubernetes/config.yaml")




# read variable from yaml file
# it should not be like php/project_root/kubernetes/config.yaml. suppose 
# it is runn from apply.py directory 
with open(f"{yaml_file_path}", "r") as t:
    data = yaml.safe_load(t)
    tag = data["data"]["IMAGE_TAG"]

commands = [
    # list of commands
    f"docker build -t zamanrahimi1368/php-app2:{tag} ./php",
    f"docker push zamanrahimi1368/php-app2:{tag}",

]
for command in commands:
    try:
        sb.run(command, check=True, shell=True)
        print(f"The command222222222222222222222222222222 {command} exected successfully \n")
        print("----------------Command------------------------")
    except sb.CalledProcessError as e:
        print(f"The error is {e}")
