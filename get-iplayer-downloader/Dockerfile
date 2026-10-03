ARG BUILD_FROM
FROM $BUILD_FROM

# Install build dependencies
RUN apk add --no-cache \
    wget \
    curl \
    git \
    make \
    cmake \
    g++ \
    linux-headers \
    zlib-dev

# Install get_iplayer
RUN wget https://raw.githubusercontent.com/get-iplayer/get_iplayer/master/get_iplayer \
    && chmod +x get_iplayer

# Install AtomicParsley
RUN git clone https://github.com/wez/atomicparsley.git \
    && cd atomicparsley \
    && cmake -B build && cmake --build build --config Release \
    && chmod +x build/AtomicParsley


FROM $BUILD_FROM

COPY --from=0 get_iplayer /usr/local/bin
COPY --from=0 atomicparsley/build/AtomicParsley /usr/local/bin

# Install runtime packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    perl \
    perl-libwww \
    perl-lwp-protocol-https \
    perl-mojolicious \
    perl-xml-libxml \
    ffmpeg

# Create working directories
RUN mkdir -p /downloads /app

# Copy run script
COPY run.py /app/run.py
RUN chmod +x /app/run.py

WORKDIR /app

CMD [ "python3", "/app/run.py" ]
