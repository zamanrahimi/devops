import boto3
import os
import credentials


os.environ['AWS_ACCESS_KEY_ID'] = credentials.access_key_id
os.environ['AWS_SECRET_ACCESS_KEY'] = credentials.secret_access_key

# Create an IAM client
iam = boto3.client('iam')

# List IAM users
response = iam.list_users()

# Print user details
print("IAM Users:")
for user in response['Users']:
    print(f"Username: {user['UserName']}, User ID: {user['UserId']}")
