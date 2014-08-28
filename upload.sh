#!/bin/bash

url=`python generate_presigned_url`
curl -v --upload-file testkey "$url"
