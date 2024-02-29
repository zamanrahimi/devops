import webbrowser
import os
import sys 
import subprocess as sb
# Get the absolute path to the current script

# import colors in absolute fasion 
# current dir
current_directory = os.path.dirname(os.path.abspath(__file__)) 
# one dir back
one_dir_back = os.path.dirname(current_directory)
# two dir back
two_dir_back = os.path.dirname(os.path.dirname(current_directory))
three_dir_back = os.path.dirname(os.path.dirname(two_dir_back))

# go inside the dirs
two_dirs_inside = os.path.join(two_dir_back, 'component', 'public')
# Add the absolute path to 'public' directory to the Python path
sys.path.append(two_dirs_inside)
sys.path.append(three_dir_back)
import colors as color



print(
    f"{color.Colors.GREEN} Build / repo phase  {color.Colors.RESET}"
)


commands = [
    
    # a_plan 
    "docker run -p 8080:8080 -p 50000:50000 --name jenkins-container -d jenkins/jenkins",
    "docker exec -it jenkins-container /bin/bash",
    "cat /var/jenkins_home/secrets/initialAdminPassword",


]

for command in commands:
    try:
        # execute main command
        sb.run(command, check=True, shell=True)
        print(
            f"{color.Colors.BLUE}----------Command {command} ---------- {color.Colors.RESET}"
        )

        print(
            f" {color.Colors.GREEN} ( {command} ) exected successfully {color.Colors.RESET} \n"
        )

    except sb.CalledProcessError as e:
        print(
            f"{color.Colors.RED}----------------Command {command} ------------------------ {color.Colors.RESET}"
        )
        print(
            f" {color.Colors.RED} The error for command ( {command} ) is {e} {color.Colors.RESET}"
        )




