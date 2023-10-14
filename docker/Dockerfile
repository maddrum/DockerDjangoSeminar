FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV DOCKYARD_PROJECT_DIR=/project
ENV DOCKYARD_USER=docker

RUN mkdir $DOCKYARD_PROJECT_DIR
RUN groupadd -r $DOCKYARD_USER -g 1000 \
	&& useradd -u 1000 -r -g $DOCKYARD_USER -d $DOCKYARD_PROJECT_DIR -s /sbin/nologin -c "Docker image user" $DOCKYARD_USER \
	&& chown -R $DOCKYARD_USER:$DOCKYARD_USER $DOCKYARD_PROJECT_DIR

ENV PATH $PATH:$DOCKYARD_PROJECT_DIR/.local/bin

# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    build-essential \
    nano \
    python3-dev  \
    python3-setuptools python3-distutils python3-pip python3-ipython \
    default-libmysqlclient-dev default-libmysqlclient-dev python3-mysqldb

COPY entrypoint.sh /docker/entrypoint.sh
RUN chmod +x /docker/entrypoint.sh

WORKDIR $DOCKYARD_PROJECT_DIR

USER $DOCKYARD_USER

EXPOSE 8000

ENTRYPOINT ["/docker/entrypoint.sh"]
