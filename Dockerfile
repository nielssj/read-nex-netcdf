FROM ubuntu:16.04

RUN apt-get update

RUN apt-get -y install python2.7
RUN apt-get -y install python-pip
RUN apt-get -y install curl
RUN apt-get -y install libnetcdf-dev
RUN apt-get -y install libhdf5-dev

RUN pip install Cython
RUN pip install pandas

RUN USE_SETUPCFG=0 HDF5_INCDIR=/usr/include/hdf5/serial HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/serial pip install netcdf4

COPY main.py /app/main.py

WORKDIR /app

CMD python main.py
