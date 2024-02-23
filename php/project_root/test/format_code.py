import subprocess as sb
import yaml

# get absolute git_command.py path

import os

# Get the absolute path to the current script
current_directory = os.path.dirname(os.path.abspath(__file__))
# Construct the relative path to the yaml file
yaml_file_path = os.path.normpath(
    os.path.join(current_directory, "../kubernetes/config.yaml")
)

import subprocess as sb
import yaml
import sys
import os


# import dependiencies
sys.path.append(os.path.join(current_directory, ".."))
from public.dependencies import colors

# read variable from yaml file
# it should not be like/kubernetes/config.yaml. suppose
# it is runn from apply.py directory
with open(f"{yaml_file_path}", "r") as t:
    data = yaml.safe_load(t)
    tag = data["data"]["IMAGE_TAG"]

print(
    f"{colors.Colors.BLUE}----------------Test Part------------------------{colors.Colors.RESET}"
)
commands = [
    # testing
    "black ../apply.py",
]
for command in commands:
    try:
        sb.run(command, check=True, shell=True)
        print(
            f"{colors.Colors.GREEN}----------------Test success commends------------------------{colors.Colors.RESET}"
        )
        print(
            f"{colors.Colors.GREEN} ({command}) exected successfully {colors.Colors.RESET} \n"
        )
    except sb.CalledProcessError as e:
        print(
            f"{colors.Colors.RED}----------------Test failed commands------------------------{colors.Colors.RESET}"
        )
        print(f"{colors.Colors.RED} The error is {e} {colors.Colors.RESET}")
