# rpi-version

Output model version of RPI that is currently running (sources: http://elinux.org/RPi_HardwareHistory)

If there are any errors, please submit an issue.

# Standalone
Run script with python 2.7
```
$ python rpi-version.py
version : 2 Model B
   date : Q1 2015
```
# Docker
Run image
```
$ docker run -it --rm nargit/rpi-version
version : 2 Model B
   date : Q1 2015
```