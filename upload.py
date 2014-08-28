#!/usr/bin/env python

import sys
import requests

url = sys.argv[1]

data='abc'

ret = requests.put(url, data=data)
print(ret)

