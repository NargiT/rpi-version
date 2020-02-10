FROM hypriot/rpi-python
LABEL maintainer="nargitinthenight@gmail.com"

ADD src/rpi_version/rpi.json .
ADD src/rpi_version .
RUN chmod +x rpi-version.py

ENV RPI_VERSION 1.1.0
ENTRYPOINT ["python", "rpi-version.py"]
