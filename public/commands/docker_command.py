import subprocess as sb
import yaml
import sys
import os
# one folder back 
sys.path.append('../')
from dependencies import colors
# get absolute git_command.py path

print(f"{colors.Colors.RED} test {colors.Colors.RESET}")


# Get the absolute path to the current script
two_directory_back = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the yaml file and PHP docker file
config_file_path = os.path.normpath(os.path.join(two_directory_back, "../../php/project_root/kubernetes/config.yaml"))
php_docker_file_path = os.path.normpath(os.path.join(two_directory_back, "../../php/project_root/php"))

# docker build -t zamanrahimi1368/php-app2:v2.9 ../../php/project_root/php


# read variable from yaml file
# it should not be like php/project_root/kubernetes/config.yaml. suppose 
# it is runn from apply.py directory 
with open(f"{config_file_path}", "r") as t:
    data = yaml.safe_load(t)
    tag = data["data"]["IMAGE_TAG"]

commands = [
    # list of commands
    f"docker build -t zamanrahimi1368/php-app2:{tag} {php_docker_file_path}",
    f"docker push zamanrahimi1368/php-app2:{tag}",

]
for command in commands:
    try:
        sb.run(command, check=True, shell=True)
        print(f"The command222222222222222222222222222222 {command} exected successfully \n")
        print("----------------Command------------------------")
    except sb.CalledProcessError as e:
        print(f"The error is {e}")
