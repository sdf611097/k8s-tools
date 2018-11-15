# Usage
```
pip3 install psutil docker
python3 checkShim.py
```
if you want to kill the shim process
```
python3 checkShim.py kill
```

# Description
Sometimes the docker container status is exited but it is still running by docker-containerd-shim, so this python script will check and delete the process. 

# Warning
I'm not sure what sideeffect of this. It is better to restart your dockerd service without livestore config.
