# FileManager
Simple File Manager written in Python3 using Tornado Web Framework

This simple application provides a basic functionality for managing files in the specific directory tree. Root directory should be specified  using the `--roothpath` command line option. Optional script parameters are:

* `--address` - IP address, which application socket will be bound to,
* `--port` - TCP port, which application socket will be bound to.

User is able to see the whole directory tree with its content (files should be able to be downloaded). After authentication (with user and password, default credentials are `admin` and `password`), user can upload new files into the current directory. 


Sample usage:

python3 run.py --address=192.168.15.67 --port=80 --rootpath=/home/telemetry/logs

