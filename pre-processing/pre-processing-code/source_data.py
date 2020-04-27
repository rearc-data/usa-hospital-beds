import os
import boto3
import urllib.request

def source_dataset(new_filename, s3_bucket, new_s3_key):

	source_dataset_url = 'https://opendata.arcgis.com/datasets/1044bb19da8d4dbfb6a96eb1b4ebf629_0'

	# Download the file from `url` and save it locally under `file_name`:
	urllib.request.urlretrieve(
		source_dataset_url + '.geojson', '/tmp/' + new_filename + '.geojson')

	urllib.request.urlretrieve(
		source_dataset_url + '.csv', '/tmp/' + new_filename + '.csv')

	s3 = boto3.client('s3')
	asset_list = []

	for filename in os.listdir('/tmp'):
		print(filename)
		s3.upload_file('/tmp/' + filename, s3_bucket, new_s3_key + '.' + filename.rsplit('.', 1)[1])
		asset_list.append(
			{'Bucket': s3_bucket, 'Key': new_s3_key + '.' + filename.rsplit('.', 1)[1]})
	
	return asset_list