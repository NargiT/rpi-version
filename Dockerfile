FROM hypriot/rpi-python
LABEL maintainer="nargitinthenight@gmail.com"

ADD rpi.json .
ADD rpi-version.py .
RUN chmod +x rpi-version.py

ENV RPI_VERSION 1.0.0
ENTRYPOINT ["python", "rpi-version.py"]
