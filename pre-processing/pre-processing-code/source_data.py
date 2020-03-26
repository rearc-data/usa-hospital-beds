import os
import pandas as pd
import boto3
from urllib.request import urlopen

source_dataset_url = "https://opendata.arcgis.com/datasets/1044bb19da8d4dbfb6a96eb1b4ebf629_0.geojson"

def source_dataset(new_filename, s3_bucket, new_s3_key):
	url = urlopen(source_dataset_url)
	output = open('/tmp/' + new_filename, 'wb')
	output.write(url.read())
	output.close()

	#uploading new s3 dataset
	s3 = boto3.client('s3')
	s3.upload_file('/tmp/' + new_filename, s3_bucket, new_s3_key)
