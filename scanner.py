#!/bin/python3

import sys;
import socket;
from datetime import datetime

if len(sys.argv) == 2:
  target = socket.gethostbyname(sys.argv[1])
else:
  print('Invalid syntax')
  print('Syntax: python3 scanner.py <ip>')
  sys.exit()

print('-' * 50)
print('Scanning target '+target);
print('Time started: '+str(datetime.now()))
print('-'*50)

try:
  for port in range(1,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target,port))
    if result == 0:
      print('Port {} is open'.format(port))
    s.close()

except KeyboardInterrupt:
  print('\n Ctrl+c pressed...Exiting program');
  sys.exit();

except sys.gaierror:
  print('Hostname could not be resolved.')
  sys.exit()

except socket.error:
  print('Couldn\'t connect to server')
  sys.exit();