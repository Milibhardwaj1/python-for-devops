import boto3

def get_connection(service):
    return boto3.client(service) #Creating a client for s3 so that it can call s3 objects


def show_buckets(s3_client):
    response = s3_client.list_buckets()

    for bucket in response["Buckets"]:
        print(bucket["Name"])

def create_bucket(s3_client, name):
    response = s3_client.create_bucket(
        Bucket=name)
        # CreateBucketConfiguration={
        #     'LocationConstraint': region
        # }
    print(response)

def upload_to_bucket(s3_client, file_path, bkt_name, key_name):
    response = s3_client.upload_file(file_path,bkt_name, key_name)
    

s3 = get_connection("s3")
show_buckets(s3)
create_bucket(s3, "rehman-bkt")
upload_to_bucket("")