# Questions

## How do I delete a S3 Bucket?

In console
- First you have to ensure you have the right permissions on the bucket.
- Check IAM role or bucket policy for `s3:DeleteBucket`. This will let you actually delete bucket

reference : https://stackoverflow.com/questions/45693897/unable-to-delete-s3-bucket

Via API

reference : https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html