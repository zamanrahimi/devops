import os

def create_directory(directory_path):
    os.makedirs(directory_path, exist_ok=True)

def create_project_structure():
    # Create the project root directory
    create_directory("project_root")

    # Change to the project root directory
    os.chdir("project_root")

    # Directories within the app directory
    app_directories = ["app/presentation", "app/application", "app/domain", "app/infrastructure", "app/utilities", "app/config", "app/tests", "app/docs", "app/deployment"]

    for directory in app_directories:
        create_directory(directory)

    # Directories within the presentation directory
    create_directory("app/presentation/views")
    create_directory("app/presentation/controllers")
    create_directory("app/presentation/static")

    # Directories within the application directory
    create_directory("app/application/service_layer")
    create_directory("app/application/use_cases")

    # Directories within the domain directory
    create_directory("app/domain/entities")
    create_directory("app/domain/value_objects")

    # Directories within the infrastructure directory
    create_directory("app/infrastructure/data_access")
    create_directory("app/infrastructure/external_services")

    # Directories within the tests directory
    create_directory("app/tests/unit")
    create_directory("app/tests/integration")

    # Directories within the deployment directory
    create_directory("app/deployment")

    # Create additional files
    for file_name in ["requirements.txt", "README.md", ".gitignore"]:
        open(file_name, 'a').close()

    # Create the devops directory and its subdirectories
    devops_directories = ["devops/docker", "devops/kubernetes", "devops/scripts"]

    for directory in devops_directories:
        create_directory(directory)

    # Create Docker-related files
    with open("devops/docker/Dockerfile", 'w') as dockerfile:
        dockerfile.write("# Your Dockerfile content goes here\n")

    # Create Kubernetes deployment files
    with open("devops/kubernetes/deployment.yaml", 'w') as deployment_yaml:
        deployment_yaml.write("# Your deployment.yaml content goes here\n")

    with open("devops/kubernetes/service.yaml", 'w') as service_yaml:
        service_yaml.write("# Your service.yaml content goes here\n")

    # Create deployment script
    with open("devops/scripts/deploy.sh", 'w') as deploy_script:
        deploy_script.write("# Your deployment script content goes here\n")

if __name__ == "__main__":
    create_project_structure()
