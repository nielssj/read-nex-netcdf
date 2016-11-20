# read-nex-netcdf
Read NASA Earth Exchange Global Daily Downscaled Projections (NEX-GDDP) dataset into Python Pandas dataframe

## Usage
You have 2 options: 

- Local (old school): Configure your local machine with all the things needed to run python-netcdf as described in their documentation (http://unidata.github.io/netcdf4-python/). This took me more than 2 hours, partly due to my unfamilarity with geospatial data formats and partly due to my particular ubuntu distribution. 
- Docker: Use the Dockerfile in this repo.

If you go with the first approach and you have are running a relatively recent Ubuntu distribution then you can peek into my Dockerfile. It should be much clearer than Unidata's documentation. If you have a different OS, refer to their documentation.

For the second approach ensure you have Docker installed (https://www.docker.com/products/docker) and then:
- Build the image
```
docker build -t read-nex-netcdf
```
- Run in a container (replace <data-path> with the local path to your data)
```
docker run -i -v <data-path>:/app/data -t read-next-netcdf
```
- Modify code in `main.py` to your needs and repeat (due to caching, build should be almost instant this time)

*NOTE: If you modify the python code to write data to the file system, make sure to output it in the `/data` directory then it will be stored on your host machine and you will have access to it after the Docker container has terminated.*
