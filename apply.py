import subprocess as sb
import yaml

# import color module
import public.dependencies.colors as color


# print(f"{color.Colors.RED}This is red text.{color.Colors.RESET}")
# exit()

# read variable from yaml file
with open("php/project_root/kubernetes/config.yaml", "r") as t:
    data = yaml.safe_load(t)
    tag = data["data"]["IMAGE_TAG"]

commands = [
    # Testing
    "black apply.py",
    # Docker
    "python public/commands/docker_command.py",
    # Kubernetes
    "kubectl apply -f php/project_root/kubernetes/config.yaml",
    "kubectl apply -f php/project_root/kubernetes/php-deployment.yaml",
    f"kubectl set image deployment/php-app-deployment-v2 php-app-container=zamanrahimi1368/php-app2:{tag}",
    "kubectl apply -f php/project_root/kubernetes/mysql-deployment.yaml",
    "kubectl apply -f php/project_root/kubernetes/persistent-volume.yaml",
    "kubectl apply -f php/project_root/kubernetes/php-service.yaml",
    # Github
    "python public/commands/git_command.py",
]

count = 1
for command in commands:
    try:
        # execute main command
        sb.run(command, check=True, shell=True)
        print(
            f"{color.Colors.BLUE}----------------Command {count} ------------------------ {color.Colors.RESET}"
        )

        print(
            f" {color.Colors.GREEN} ( {command} ) exected successfully {color.Colors.RESET} \n"
        )

        count += 1

    except sb.CalledProcessError as e:
        print(
            f"{color.Colors.RED}----------------Command {count} ------------------------ {color.Colors.RESET}"
        )
        print(
            f" {color.Colors.RED} The error for command ( {command} ) is {e} {color.Colors.RESET}"
        )
