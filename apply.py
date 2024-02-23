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
    f"docker build -t zamanrahimi1368/php-app2:{tag} ./php/project_root/php",
    f"docker push zamanrahimi1368/php-app2:{tag}",
    # Kubernetes
    "kubectl apply -f php/project_root/kubernetes/config.yaml",
    "kubectl apply -f php/project_root/kubernetes/php-deployment.yaml",
    f"kubectl set image deployment/php-app-deployment-v2 php-app-container=zamanrahimi1368/php-app2:{tag}",
    "kubectl apply -f php/project_root/kubernetes/mysql-deployment.yaml",
    "kubectl apply -f php/project_root/kubernetes/persistent-volume.yaml",
    "kubectl apply -f php/project_root/kubernetes/php-service.yaml",
    # Github
    "python git_commands.py",
]

count = 1
for command in commands:
    try:
        sb.run(command, check=True, shell=True)
        print(
            f" {color.Colors.RED} The command {command} exected successfully {color.Colors.RESET} \n"
        )
        print(f"----------------Command {count} ------------------------")
        count += 1
    except sb.CalledProcessError as e:
        print(f"The error is {e}")
