#!/bin/bash

echo '********************upload********************'
url=`python generate_presigned_url.py PUT`
python upload.py $url

echo '********************download********************'
url=`python generate_presigned_url.py GET`
python download.py $url

echo '********************delete********************'
python delete.py
