#in this file i would be making a python file having boto3 to remove/delete the stale snapshot which were taken during a 
#ec2 instance and now no ec2 and its volume are left after deleting the ec2 instance. 
#USE AWS or you can use localstack + AWSCLI for the run 


import boto3

#you can change the name of teh lamdba handler but make sure to configure the same in AWS also . 
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')        #select the service you want

    # Get all EBS snapshots
    response = ec2.describe_snapshots(OwnerIds=['self'])      #taken as it is from the boto3 docs with few tweaks

    # Get all active EC2 instance IDs
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_instance_ids = set()

    #using basic python to get the job done 
    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    # Iterate through each snapshot and delete if it's not attached to any volume or the volume is not attached to a running instance
    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

        if not volume_id:
            # Delete the snapshot if it's not attached to any volume
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
        else:
            # Check if the volume still exists
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found (it might have been deleted)
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")


          #now you can basically set the cronjob or do it manually everytime to delete/notify the stale snapshots
          #during the lambda function calling it might fail before of the permission, make sure to give everything from the policies or 
          #create new policies
          #before calling everythgin make sure to have a ec2 instance running and also create a volume if now made (highly unlikely wont be made)
          #also create a snapshot for that isntance/ 
          #make sure to delete every resource or cronjob, snapshots (i mean everything) after work is completeted to not get chareged if using AWS real.
          #no efforts for the same on localstack
          
