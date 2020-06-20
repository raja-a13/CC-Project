# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
import boto3
from boto3.dynamodb.conditions import Key, Attr
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


def test(request):
        myfile = request.FILES['sentFile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        f = request.FILES['sentFile']
        f="./media/"+str(myfile)
        s3 = boto3.client('s3')
        bucket = 'justart'
        file_name = str(f)
        key_name = str(myfile)
        s3.upload_file(file_name, bucket, key_name)
        bucket_location = boto3.client('s3').get_bucket_location(Bucket=bucket)
        link = "https://s3-ap-south-1.amazonaws.com/{0}/{1}".format(bucket,key_name)
        print(f"link : {link} \n")
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('demo')
        response = table.put_item(
            Item={
                'link':link,
            }
        )
        args = {}
        args['link'] = link
        return render(request,'Link.html',args)
def home(request):
    return render(request,'home.html')

