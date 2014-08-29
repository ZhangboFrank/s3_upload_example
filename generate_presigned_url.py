#!/usr/bin/env python

import sys
import boto.s3

from conf import region, bucket, key, checksum_header_name, data_checksum

method = sys.argv[1]

expires_in = 600

headers = {}
headers['x-amz-server-side-encryption-customer-algorithm'] = 'AES256'

if method == 'PUT':
    headers[checksum_header_name] = data_checksum

conn = boto.s3.connect_to_region(region)

url = conn.generate_url(expires_in, method, bucket, key, headers)

print(url)
