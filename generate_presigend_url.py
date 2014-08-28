#!/usr/bin/env python

import boto.s3

region = 'cn-north-1'

expires_in = 600
method = 'PUT'
bucket = 'bigdata'
key = 'testkey'

conn = boto.s3.connect_to_region(region)

url = conn.generate_url(expires_in, method, bucket, key)

print(url)
