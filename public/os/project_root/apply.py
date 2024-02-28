import subprocess as sb
import yaml

# import color module
import public.dependencies.colors as color


# print(f"{color.Colors.RED}This is red text.{color.Colors.RESET}")
# exit()

# read variable from yaml file
with open("kubernetes/config.yaml", "r") as t:
    data = yaml.safe_load(t)
    tag = data["data"]["IMAGE_TAG"]

commands = [
    
    # Testing
    "black test/unit_test.py",

    # Docker
    "python public/commands/docker_command.py",
    # Kubernetes
    "kubectl apply -f kubernetes/config.yaml",
    "kubectl apply -f kubernetes/secret.yaml",
    "kubectl apply -f kubernetes/php-deployment.yaml",
    f"kubectl set image deployment/php-app-deployment-v2 php-app-container=zamanrahimi1368/php-app2:{tag}",
    "kubectl apply -f kubernetes/mysql-deployment.yaml",
    "kubectl apply -f kubernetes/persistent-volume.yaml",
    "kubectl apply -f kubernetes/php-service.yaml",
    # Github
    "python public/commands/git_command.py",
    # less import comments
    # lsit of kubernetes objects
    "python public/commands/kubernetes_objects.py",

    # Get URL 
    "python public/commands/get_url.py",
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
