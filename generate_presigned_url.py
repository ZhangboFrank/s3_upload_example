#!/usr/bin/env python

import sys
import boto.s3

from conf import key, checksum_header_name, data_checksum

region = sys.argv[1]
bucket = sys.argv[2]
method = sys.argv[3]

expires_in = 600

headers = {}
headers['x-amz-server-side-encryption-customer-algorithm'] = 'AES256'

if method == 'PUT':
    headers[checksum_header_name] = data_checksum

conn = boto.s3.connect_to_region(region)

url = conn.generate_url(expires_in, method, bucket, key, headers)

print(url)
