import boto3

FILES = [
    "results.json",
    "daily_wordle.json",
    "daily_connections.json",
]

s3 = boto3.client('s3')
for filename in FILES:
    s3.download_file('wgb-s3', filename, filename)
