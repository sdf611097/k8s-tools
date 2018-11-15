#!/usr/bin/env python3
import psutil, docker ,os, sys

exited = 0
client = docker.from_env()
for p in psutil.process_iter():
    cmd = p.cmdline()
    if len(cmd)>0 and 'docker-containerd-shim' in cmd[0]:
      try:
        id = cmd[1]
        status = client.containers.get(id).status
        print(p.pid, id[0:5], status.lower())
        if status.lower() == 'exited':
          if len(sys.argv) == 2 and sys.argv[1] == 'kill':
            print('kill')
            os.kill(p.pid, 9)
          exited +=1
      except Exception as e:
        print(e)

print('total', exited, 'exited but it is running by shim')
