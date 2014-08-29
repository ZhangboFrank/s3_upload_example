#!/usr/bin/env python

import hashlib
# region = 'cn-north-1'
# bucket = 'bigdata'

region = 'us-west-2'
bucket = 'yupeng'

key = 'testkey'

data = 'abc'

sse_key = '0' * 32

checksum_header_name = "x-amz-meta-checksum"
data_checksum = hashlib.md5(data).hexdigest()
