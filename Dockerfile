############################################################
# Dockerfile to run a Django-based web application
# Based on an Ubuntu Image
############################################################

# Set the base image to use to Ubuntu
FROM ubuntu:14.04

# Set the file maintainer (your name - the file's author)
MAINTAINER Svetlana Margetova

# Set env variables used in this Dockerfile
# Local directory with project source
ENV UFX_SRC=ufx_devel

# Directory in container for all project files
ENV UFX_SRVHOME=/srv
# Directory in container for project source files
ENV UFX_SRVPROJ=/srv/ufx_devel

# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y libpq-dev
RUN apt-get install -y python-dev
RUN pip3 install psycopg2

# Create application subdirectories
WORKDIR $UFX_SRVHOME
RUN mkdir media static logs
VOLUME ["$UFX_SRVHOME/media/", "$UFX_SRVHOME/logs/", "$UFX_SRVHOME/static/"]

# Copy application source code to SRCDIR
COPY $UFX_SRC $UFX_SRVPROJ

# Install Python dependencies
RUN pip3 install -r $UFX_SRVPROJ/requirements.txt

# Port to expose
EXPOSE 8000

# Copy entrypoint script into the image
WORKDIR $UFX_SRVPROJ
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
