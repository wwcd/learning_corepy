#! python

import re
import pdb

pdb.set_trace()
m = re.match('foo', '1foo')
print m

if m is not None:
    print m.group()

m = re.search('foo', '1foo')
print m

if m is not None:
    print m.group()
