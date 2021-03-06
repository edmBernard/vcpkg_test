FROM ubuntu:16.04
LABEL maintainer="Erwan BERNARD https://github.com/edmBernard/DockerFiles"


RUN apt-get clean && apt-get update && apt-get upgrade -y && \
    apt-get install -y \
        build-essential software-properties-common cmake git nano \
        curl wget rsync unzip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install GCC 7
RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y && \
    apt-get update -y && \
    apt-get install -y gcc-7 g++-7 \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV CC=/usr/bin/gcc-7
ENV CXX=/usr/bin/g++-7

# Configuration
ENV HOME "/home/dev"
RUN mkdir -p "$HOME"

ENV LIB_DIR "$HOME/lib"
RUN mkdir -p "$LIB_DIR"

WORKDIR $HOME/host

RUN ln -snf /bin/bash /bin/sh
RUN cp /root/.bashrc $HOME/.bashrc && \
    sed -i 's/#force_color_prompt=yes/force_color_prompt=yes/g' ~/.bashrc

# Install cmake 3.11
RUN cd $HOME/lib && \
    wget https://cmake.org/files/v3.11/cmake-3.11.1.tar.gz && \
    tar -zxvf cmake-3.11.1.tar.gz && \
    cd cmake-3.11.1 && \
    cmake . && \
    make && \
    make install

# install vcpkg for local folder to allow custom version
COPY vcpkg vcpkg
WORKDIR $HOME/host/vcpkg

RUN ./bootstrap-vcpkg.sh && \
    ./vcpkg integrate install

CMD ["/bin/bash"]
