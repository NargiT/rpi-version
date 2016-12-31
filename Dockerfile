FROM hypriot/rpi-python
MAINTAINER Tig Tch <nargitinthenight@gmail.com>

ADD rpi.json .
ADD rpi-version.py .
RUN chmod +x rpi-version.py

ENTRYPOINT ["python", "rpi-version.py"]