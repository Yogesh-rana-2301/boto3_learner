# AWS EBS Stale Snapshot Cleaner

This repository contains a **Python AWS Lambda function** that automatically detects and deletes **stale EBS snapshots**.

## What is a Stale Snapshot?
A snapshot is considered stale when:
- It is not attached to any EBS volume.
- Its associated EBS volume no longer exists.
- The volume exists but is not attached to any running EC2 instance.

## How It Works
The script uses **Boto3** (AWS SDK for Python) to interact with AWS EC2 services and can be run either:
- **On AWS Lambda** (recommended for automation).
- **Locally** using **LocalStack** and **AWS CLI** for safe testing without incurring AWS costs.

## Key Features
- Scans all snapshots owned by your AWS account.
- Identifies unused or orphaned snapshots.
- Deletes them to save storage costs and keep your AWS account clean.
- Can be scheduled via **CloudWatch Events (cron)** for periodic cleanup.

## Requirements
- **AWS CLI** configured with the correct credentials, or LocalStack for local testing.
- Necessary IAM permissions to:
  - Describe EC2 instances, volumes, and snapshots.
  - Delete snapshots.
- Python 3.x and the `boto3` package.

## Usage
1. Deploy the function in AWS Lambda or run locally.
2. Ensure IAM permissions are granted for EC2 actions.
3. Optionally, set up a **cron schedule** to run automatically.
4. Always test in **LocalStack** before using in production to avoid accidental data loss.
