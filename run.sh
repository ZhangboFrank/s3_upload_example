#!/bin/bash

url=`python generate_presigned_url.py`
python upload.py $url
