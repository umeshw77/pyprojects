#!/usr/bin/python

import re

SRC_DST=r'(?:any|host\s+\S+|[0-9\.]+\s[0-9\.]+)\s+'
#  permit|deny  udp|tcp src dst
PORT_COMMON = r'(?:permit|deny)\s+(udp|tcp)\s+' + SRC_DST + SRC_DST

#  permit|deny  udp|tcp src dst port|range <num1>
REGEX_PORT = re.compile(PORT_COMMON + r'(?:eq|lt|gt|le|ge|ne|range)\s+(\d+)')

s = "permit tcp any any"
#m = REGEX_PORT.match(s)
m = re.compile(r'permit (tcp|udp) \S+ \S+').match(s)
print (m.group(1))
print (m.end(1))

