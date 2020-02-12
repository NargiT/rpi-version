# rpi-version

![Tests](https://github.com/NargiT/rpi-version/workflows/Tests/badge.svg?event=push)

Output model version of RPI that is currently running.
sources: [wiki](http://elinux.org/RPi_HardwareHistory)

If there are any errors, please submit an issue.

## Standalone

Run script

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
