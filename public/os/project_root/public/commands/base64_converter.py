import base64

database_name = "db2"
encoded_database_name = base64.b64encode(database_name.encode()).decode()
print(f"Base64 Encoded Database Name: {encoded_database_name}")
