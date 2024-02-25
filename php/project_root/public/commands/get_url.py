import subprocess

def get_port_number(service_name):
    try:
        # Run kubectl get services and capture the output
        result = subprocess.run(['kubectl', 'get', 'services'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')

        # Find the line containing the service name
        service_line = next(line for line in output_lines if service_name in line)

        # Split the line and extract the port number
        port_number = service_line.split()[4].split(':')[1].split('/')[0]

        return port_number
    except Exception as e:
        print(f"Error: {e}")
        return None

# Replace 'php-app-service-v2' with your actual service name
service_name = 'php-app-service-v2'
port_number = get_port_number(service_name)

if port_number is not None:
    print(f"The URL for {service_name} is:http://localhost:{port_number}")
else:
    print(f"Unable to retrieve the port number for {service_name}")
