ARG BUILD_FROM
FROM $BUILD_FROM

# Install required packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    perl \
    perl-libwww \
    perl-lwp-protocol-https \
    perl-mojolicious \
    perl-xml-libxml \
    ffmpeg \
    wget \
    curl

# Install get_iplayer
RUN wget https://raw.githubusercontent.com/get-iplayer/get_iplayer/master/get_iplayer -O /usr/local/bin/get_iplayer \
    && chmod +x /usr/local/bin/get_iplayer

# Create working directories
RUN mkdir -p /downloads /app

# Copy run script
COPY run.py /app/run.py
RUN chmod +x /app/run.py

WORKDIR /app

CMD [ "python3", "/app/run.py" ]
