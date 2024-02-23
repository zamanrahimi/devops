import base64

# Replace these values with your actual MySQL root password and database name
mysql_root_password = "your_mysql_password"
mysql_database_name = "db2"

# Encode the values to base64
encoded_root_password = base64.b64encode(mysql_root_password.encode()).decode()
encoded_database_name = base64.b64encode(mysql_database_name.encode()).decode()

print(f"Encoded Root Password: {encoded_root_password}")
print(f"Encoded Database Name: {encoded_database_name}")
