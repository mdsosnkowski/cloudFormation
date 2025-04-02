# Web Scraper Notes and Log
For markdown preview: Ctrl-K V  
For promt shorting in CLI: export PS1="\W\$ "  
[Design](https://youtu.be/51r3zPOun5g?si=MR2AjWEhBgGIDdSw)
## APRIL 2025
#### Wed 2
How to associate an SG to the instance Subnet? A: Reference the VPC in the SG config with VpcId: !Ref myVCP.
Test login to EC2 host with Connect - WORKING!!  
How to connect to Database port on tcp 3306? A:
## MARCH 2025
#### Fri 28
Created basic EC2 for testing the "connect" feature of the console. it did not work so read: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-prerequisites.html.
#### Thu 27
Played with SQS queues to understand disributed data entry.  
#### Wed 26
Combined RDS, EC2 Profiles, and all else into one new build called webScraper_V1.yaml.  
Next: Build scraper code with python flask on replit and run on the ec2 instances manually.  
AFTER: combine in the user data of the ec2 instance the python code to run when stack built.  
FINAL: Add cloudwatch monitoring.
#### Tue 25
Create login access keys to session onto the ec2 instance with "connect".  
Test from EC2 access to S3 and RDS.
#### Mod 24
Create new policy to allow access to RDS Note, cannot it is done on the RDS instance with username/password. Can use AWS Secrest Nanager for future iterations.- DONE for now.  
Create EC2 account keys to allows ssh access.  
#### Thu 20
Fix IAM issues 
In AWS CloudFormation, CAPABILITY_IAM is a required capability when your stack includes resources that create or modify AWS Identity and Access Management (IAM) roles, policies, or users. In AWS CLI
When using the AWS CLI to create or update a stack that includes IAM resources, you must specify the capability using the --capabilities flag:
#### Wed 19
For IAM do the following:  
1. EC2 write permissions to S3  
2. EC2 read/write permissions to RDS
In AWS CloudFormation, you grant an EC2 instance read/write access to an S3 bucket by:
  1. Creating an IAM Role with an IAM Policy that allows S3 access.
  2. Attaching the IAM Role to an Instance Profile.
  3. Associating the Instance Profile with the EC2 instance.
#### Fri 14
Fixed PublicIP output not working by listing "private" 
Re-test RDS build if located servers in private subnets of VPC.  
- Confirmed, tested, and working.  
#### Thu 13
RDS in mulitiple AZ for active and standby SQL needed.
Done by need to check as build did not finish but no RDS issues!
#### Wed 12
Debug VPC lodding: issue was misspelling of "Tags" which caused rollback of build eventhough passed validation.
Conclusion: valdation does not catch spelling mistakes and is limited in checking for quality
#### Tue 11
Create VPC with internet gateway and db in private and web in public
Create CloudWatch
#### Wed 5
Create S3 bucket for holding images in file: webScraper_EC2_S3.yaml
Created RDS minimal build with new file called: webScraper_EC2_S3_RDS.yaml
#### Tue 4
Changed all names to reflect the name of the project "webScraper" with a list of the resources being provisioned of each step. As well adding in assertions to check if the code is correct.
#### Mon 3
Create the RDS Datbase backend.
## FEBRUARY 2025
#### M 24 - Path name format for stack creation
Determine the correct windows/bash path to create stack from AWS CLI
To get an AWS AMI image for us-east-1 in BASH use the AWS CLI command: aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --region us-east-1 --query 'Parameters[0].Value' --output text
Output: ami-0c104f6f4a5d9d1d5

aws cloudformation validate-template --template-body file:///mnt/c/Users/Joasia/Documents/MikeStuff/CloudFormationProjects/cloudFormation/project1-a.yaml

aws cloudformation create-stack   --stack-name my-stack   --template-body  file:///mnt/c/Users/Joasia/Documents/MikeStuff/CloudFormationProjects/cloudFormation/project1-a.yaml

NOTE: do not put the parameters in the cli command as theses are in the config
NOTE: try to use a non-hardcodded Instance type

#### Sat 22 - EC2 basic instance setup
Used AI to help and CFN docs to clarify the use of /
the ami generic version: ImageId: !Sub "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}"

 myVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: 'true'
      EnableDnsSupport: 'true'
  mySubnetPublic:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref myVPC
      CidrBlock: 10.0.0.0/24
  mySubnetPrivate:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref myVPC
      CidrBlock: 10.0.1.0/24