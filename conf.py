#!/usr/bin/env python

import hashlib

key = 'testkey'
data = 'hello world'
sse_key = '0' * 32
checksum_header_name = "x-amz-meta-checksum"
data_checksum = hashlib.md5(data).hexdigest()
