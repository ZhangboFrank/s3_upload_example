#!/usr/bin/env python

import sys
import base64
import hashlib
import requests

url = sys.argv[1]

sse_key = '0' * 32

sse_key_base64 = base64.standard_b64encode(sse_key)
sse_key_md5 = hashlib.md5(sse_key).digest()
sse_key_md5_base64 = base64.standard_b64encode(sse_key_md5)

headers = {}
headers['x-amz-server-side-encryption-customer-key'] = sse_key_base64
headers['x-amz-server-side-encryption-customer-key-MD5'] = sse_key_md5_base64

ret = requests.get(url, headers=headers)
print(ret)
print(ret.text)
