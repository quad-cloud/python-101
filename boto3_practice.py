import boto3

def list_buckets():
    s3_resource = boto3.resource('s3')
    my_buckets = s3_resource.buckets.all()
    for bucket in my_buckets:
        print(bucket.name)

def create_bucket(bucket_name):
    s3_resource = boto3.resource('s3')
    s3_bucket = s3_resource.create_bucket(Bucket=bucket_name)
    print(s3_bucket.name)

def delete_bucket(bucket_name):
    s3_resource = boto3.resource('s3')
    s3_bucket = s3_resource.Bucket(bucket_name)
    s3_bucket.delete()

def delete_bucket_content(bucket_name):
    s3_resource = boto3.resource('s3')
    s3_objects = s3_resource.Bucket(bucket_name).objects.all()
    for s3_object in s3_objects:
        s3_object_name = s3_object.key
        # print(s3_object_name)
        object = s3_resource.Object(bucket_name,s3_object_name)
        # print(object)
        object.delete()


def list_ec2_instances():
    ec2_resource = boto3.resource('ec2')
    instances_list = ec2_resource.instances.all()
    for instance in instances_list:
        print(instance.id)

def create_instance():
    ec2_resource = boto3.resource('ec2')
    ec2_instances = ec2_resource.create_instances(
        ImageId='ami-97785bed',
        InstanceType='t1.micro',
        MinCount=1,
        MaxCount=1)
    for instance in ec2_instances:
        print(instance.id)

def delete_instance(instance_id):
    ec2_resource = boto3.resource('ec2')
    ec2_instance = ec2_resource.Instance(instance_id)
    ec2_instance.terminate()

def main():
    delete_bucket_content('cc-04-05-2017')

if(__name__ == "__main__"):
    main()