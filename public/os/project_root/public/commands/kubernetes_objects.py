import os
import yaml
import csv
import sys 


# Get the absolute path to the current script
current_directory_back = os.path.dirname(os.path.abspath(__file__))
kubernetes_folder_path = os.path.normpath(os.path.join(current_directory_back, "../../kubernetes"))
csv_file_path = os.path.normpath(os.path.join(current_directory_back, "../dependencies/csv/kubernetes_objects.csv"))


def get_object_info(yaml_content):
    metadata = yaml_content.get('metadata', {})
    object_type = yaml_content.get('kind')
    object_name = metadata.get('name')
    return object_type, object_name

def process_yaml_file(file_path, csv_writer):
    with open(file_path, 'r') as yaml_file:
        try:
            yaml_contents = list(yaml.safe_load_all(yaml_file))
            for i, yaml_content in enumerate(yaml_contents, start=1):
                object_type, object_name = get_object_info(yaml_content)
                if object_name:
                    csv_writer.writerow([object_type, object_name])
                else:
                    print(f"File: {file_path}, Document: {i}, Object Name not found in metadata.")
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file {file_path}: {e}")

def list_kubernetes_objects(folder_path, csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["object_type", "object_name"])
        
        for filename in os.listdir(folder_path):
            if filename.endswith(".yaml"):
                file_path = os.path.join(folder_path, filename)
                process_yaml_file(file_path, csv_writer)



# List Kubernetes objects and save to CSV
list_kubernetes_objects(kubernetes_folder_path, csv_file_path)
