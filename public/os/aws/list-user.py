import boto3
import os


# Create an IAM client
iam = boto3.client('iam')

# List IAM users
response = iam.list_users()

# Print user details
print("IAM Users:")
for user in response['Users']:
    print(f"Username: {user['UserName']}, User ID: {user['UserId']}")
