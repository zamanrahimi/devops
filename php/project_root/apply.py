import subprocess as sb
import yaml


# read variable from yaml file
with open("kubernetes/config.yaml", "r") as t:
    data = yaml.safe_load(t)
    tag = data["data"]["IMAGE_TAG"]

commands = [
    # Testing
    "black apply.py",
    # Docker
    f"docker build -t zamanrahimi1368/php-app2:{tag} ./php",
    f"docker push zamanrahimi1368/php-app2:{tag}",
    # Kubernetes
    "kubectl apply -f kubernetes/config.yaml",
    "kubectl apply -f kubernetes/php-deployment.yaml",
    f"kubectl set image deployment/php-app-deployment-v2 php-app-container=zamanrahimi1368/php-app2:{tag}",
    "kubectl apply -f kubernetes/mysql-deployment.yaml",
    "kubectl apply -f kubernetes/persistent-volume.yaml",
    "kubectl apply -f kubernetes/php-service.yaml",
    # Github
    "python ../../git_commands.py",
]
for command in commands:
    try:
        sb.run(command, check=True, shell=True)
        print(f"The command {command} exected successfully \n")
        print("----------------Command------------------------")
    except sb.CalledProcessError as e:
        print(f"The error is {e}")
