import subprocess as sb
import yaml


# read variable from yaml file
with open("kubernetes/config.yaml", "r") as t:
    data = yaml.safe_load(t)
    tag = data["data"]["IMAGE_TAG"]


w = "../../"
git_add_command = [
    "git add .",
    f"git commit -m '.{tag}.'",
    "git push",
]


commands = [
    # testing
    "black apply.py",
    *git_add_command,
    # "cd ../.. git commit -m '. Current application verison: {tag}.'",
    # "cd ../.. git push",
    # Docker
    f"docker build -t zamanrahimi1368/php-app2:{tag} ./php",
    f"docker push zamanrahimi1368/php-app2:{tag}",
    # kubernetes
    "kubectl apply -f kubernetes/config.yaml",
    "kubectl apply -f kubernetes/php-deployment.yaml",
    f"kubectl set image deployment/php-app-deployment-v2 php-app-container=zamanrahimi1368/php-app2:{tag}",
    "kubectl apply -f kubernetes/mysql-deployment.yaml",
    "kubectl apply -f kubernetes/persistent-volume.yaml",
    "kubectl apply -f kubernetes/php-service.yaml",
]
for command, git_add_command in zip(commands, git_add_command):
    try:
        if git_add_command in command:
            sb.run(command, check=True, shell=True, cwd=w)
        else:
            sb.run(command, check=True, shell=True)
        print(f"The command {command} executed successfully \n")
        print("----------------Command------------------------")

    except sb.CalledProcessError as e:
        print(f"The error is {e}")
