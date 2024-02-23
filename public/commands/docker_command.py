import subprocess as sb
import yaml
import sys
import os




# Get the absolute path to the current script
current_directory_back = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the yaml file and PHP docker file
config_file_path = os.path.normpath(os.path.join(current_directory_back, "../../php/project_root/kubernetes/config.yaml"))
php_docker_file_path = os.path.normpath(os.path.join(current_directory_back, "../../php/project_root/app"))

# import dependiencies 
sys.path.append(os.path.join(current_directory_back, '..'))
from dependencies import colors

# docker build -t zamanrahimi1368/php-app2:v2.9 ../../php/project_root/php


# read variable from yaml file
# it should not be like php/project_root/kubernetes/config.yaml. suppose 
# it is runn from apply.py directory 
with open(f"{config_file_path}", "r") as t:
    data = yaml.safe_load(t)
    tag = data["data"]["IMAGE_TAG"]
    
print(f"{colors.Colors.BLUE}----------------Docker Part------------------------{colors.Colors.RESET}")
commands = [
    # list of commands
    f"docker build -t zamanrahimi1368/php-app2:{tag} {php_docker_file_path}",
    f"docker push zamanrahimi1368/php-app2:{tag}",

]
for command in commands:
    try:
        sb.run(command, check=True, shell=True)
        print(f"{colors.Colors.GREEN}----------------Docker success commends------------------------{colors.Colors.RESET}")
        print(f"{colors.Colors.GREEN} ({command}) exected successfully {colors.Colors.RESET} \n")

    except sb.CalledProcessError as e:
        print(f"{colors.Colors.RED}----------------Docker failed commands------------------------{colors.Colors.RESET}")
        print(f"{colors.Colors.RED} The error is {e} {colors.Colors.RESET}")
