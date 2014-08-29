#!/bin/bash

if [ -z "$1" ]; then
	echo "specific a region"
	exit 1
fi

region="$1"

if [ -z "$2" ]; then
	echo "specific a bucket"
	exit 1
fi

bucket="$2"

echo '********************upload********************'
url=`python generate_presigned_url.py "$region" "$bucket" PUT`
python upload.py $url

echo '********************download********************'
url=`python generate_presigned_url.py "$region" "$bucket" GET`
python download.py $url

echo '********************delete********************'
python delete.py "$region" "$bucket"
