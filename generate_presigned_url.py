#!/usr/bin/env python

import sys
import boto.s3

from conf import region, bucket, key

method = sys.argv[1]

expires_in = 600

headers = {}
headers['x-amz-server-side-encryption-customer-algorithm'] = 'AES256'

conn = boto.s3.connect_to_region(region)

# url = conn.generate_url_sigv4(expires_in, method, bucket, key, headers)
url = conn.generate_url(expires_in, method, bucket, key, headers)

print(url)
