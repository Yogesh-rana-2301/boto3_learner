#pip install boto3
import boto3
botocore-exceptions #for problem encountrering


#https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

#find the service needed
client =boto3.client('s3')    #common syntax for ec3 do ec2
#or
resource=boto3.resource('s3')

#can remove the non reqired fields
#create bucket
response = client.create_bucket(
    ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
    Bucket='baby-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'af-south-1'|'ap-east-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'ap-south-1'|'ap-south-2'|'ap-southeast-1'|'ap-southeast-2'|'ap-southeast-3'|'ap-southeast-4'|'ap-southeast-5'|'ca-central-1'|'cn-north-1'|'cn-northwest-1'|'EU'|'eu-central-1'|'eu-central-2'|'eu-north-1'|'eu-south-1'|'eu-south-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'il-central-1'|'me-central-1'|'me-south-1'|'sa-east-1'|'us-east-2'|'us-gov-east-1'|'us-gov-west-1'|'us-west-1'|'us-west-2',
        'Location': {
            'Type': 'AvailabilityZone'|'LocalZone',
            'Name': 'string'
        },
        'Bucket': {
            'DataRedundancy': 'SingleAvailabilityZone'|'SingleLocalZone',
            'Type': 'Directory'
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    },
    GrantFullControl='string',
    GrantRead='string',
    GrantReadACP='string',
    GrantWrite='string',
    GrantWriteACP='string',
    ObjectLockEnabledForBucket=True|False,
    ObjectOwnership='BucketOwnerPreferred'|'ObjectWriter'|'BucketOwnerEnforced'
)



#get bucket acl
response = client.get_bucket_acl(
    Bucket='string',
    ExpectedBucketOwner='string'
)
