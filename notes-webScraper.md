# Web Scraper Notes and Log
For markdown preview: Ctrl-K V
For promt shorting in CLI: export PS1="\W\$ "
 
## MARCH 2025

#### Tuesday 4
Changed all names to reflect the name of the project "webScraper" with a list of the resources being provisioned of each step. As well adding in assertions to check if the code is correct.
#### Monday 3
Create the RDS Datbase backend.


## FEBRUARY 2025
#### Mon 24 - Path name format for stack creation
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
