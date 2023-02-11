# Empty list of AWS services

aws_services = []
print (aws_services)
print ("The list is currently empty.")

# Populate a list with AWS services 
aws_services.insert(0,'EC2')
aws_services.insert(1,'IAM')
aws_services.insert(2,'S3')
aws_services.insert(3,'VPC')
aws_services.insert(4,'CLOUD9')
print (aws_services)

# Print the list and the length
print(len(aws_services))

# Add an AWS service and print the list with the length
aws_services.insert(5, 'CLOUDWATCH')
print(aws_services)
print(len(aws_services))

# Remove two services and print the list with the new length
del aws_services[1:3]
print(aws_services)
print(len(aws_services))