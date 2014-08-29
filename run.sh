#!/bin/bash

url=`python generate_presigned_url.py PUT`
python upload.py $url

url=`python generate_presigned_url.py GET`
python download.py $url

python delete.py
