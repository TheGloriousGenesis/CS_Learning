This is going to be my diary of how I went from knowing jack shit about AWS to completing and passing my AWS Machine Learning speciality course with flying colours


## Get accustomed to the console management in AWS

## Play with uploading and downloading and deleting S3 buckets / Data 

### Via Console
reference AWS tutorial: https://aws.amazon.com/getting-started/hands-on/backup-files-to-amazon-s3/

### Via S3 CLI

Reference AWS tutorial: https://aws.amazon.com/getting-started/hands-on/backup-to-s3-cli/

Pre-requisites: Understanding a little about IAM roles in AWS. Not necessarily but if one wants to understand more secure ways to set up AWS CLI very important
Reference AWS tutorial: https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-assign-account-access-user.html
Reference AWS tutorial: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html

Fixes to cli tutorial: 
1. Step that states `Click the Add user button` should be replaced with `Click the Create User button`
2. There are no options to select `Programmatic access` to your role after creating name for bucket. I believe this access is default in any role you create?
3. It has changed from `Attach exisiting policies directly` > `Attach policies directly`
4. There is no Review button explicitly, after you have selected your policy/policies and click next review your selection then click `Create user` button
5. Credentials are not automatically created. You have to go to your new user, select `Security crednetials > Access keys > create keys`
6. Tutorial doesn't tell you how to delete bucket (only data in bucket). Follow the tutorial: https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html or execute `aws s3 rb s3://bucket-name`

