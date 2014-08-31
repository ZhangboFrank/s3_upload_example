#!/usr/bin/env python

import sys
import boto.s3
from boto.s3.key import Key

from conf import key

region = sys.argv[1]
bucket = sys.argv[2]

c = boto.s3.connect_to_region(region)
b = c.get_bucket(bucket)
k = Key(b)
k.key = key
k.delete()
