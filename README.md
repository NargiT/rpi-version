# rpi-version

[![Build Status](https://travis-ci.org/NargiT/rpi-version.svg?branch=master)](https://travis-ci.org/NargiT/rpi-version)

Output model version of RPI that is currently running.
sources: [wiki](http://elinux.org/RPi_HardwareHistory)

If there are any errors, please submit an issue.

## Standalone

Run script with python 2.7

```sh
$ python rpi-version.py
version : 2 Model B
   date : Q1 2015
```

## Docker

Run image

```sh
$ docker run -it --rm nargit/rpi-version
version : 2 Model B
   date : Q1 2015
```