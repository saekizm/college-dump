#!/usr/bin/env python3

import sys

from q3_052 import build_dictionary, extract_range

d = build_dictionary(sys.stdin)

nd = extract_range(d, 5, 15)

for (k, v) in sorted(nd.items()):
  print(f'{k} : {v}')
