#!/usr/bin/env python

import boto.s3

from conf import region, bucket, key

expires_in = 600
method = 'PUT'

headers = {}
headers['x-amz-server-side-encryption-customer-algorithm'] = 'AES256'

conn = boto.s3.connect_to_region(region)

# url = conn.generate_url_sigv4(expires_in, method, bucket, key, headers)
url = conn.generate_url(expires_in, method, bucket, key, headers)

print(url)
