FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

# Install "software-properties-common" (for the "add-apt-repository")
RUN apt-get update && apt-get install -y \
    software-properties-common
# Add the "JAVA" ppa
RUN add-apt-repository -y \
    ppa:webupd8team/java

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get install -y git && \
    apt-get install -y subversion && \
    apt-get install -y time && \
    apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# Install Python 3
RUN apt-get install -y python3.9 python3.9-distutils python3-pip python3-apt

# Install pipenv
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN export LC_ALL
RUN export LANG

# Setup plm-repair-them-all
RUN mkdir /repair
RUN mkdir /plm-repair-them-all
COPY benchmarks /plm-repair-them-all/benchmarks
COPY data /plm-repair-them-all/data
COPY src /plm-repair-them-all/src
COPY .env /plm-repair-them-all/.env
COPY .git /plm-repair-them-all/.git
COPY .gitmodules /plm-repair-them-all/.gitmodules
COPY Pipfile /plm-repair-them-all/Pipfile
COPY Pipfile.lock /plm-repair-them-all/Pipfile.lock
COPY setup.sh /plm-repair-them-all/setup.sh
RUN cd /plm-repair-them-all && python3.9 -m pip install pipenv
RUN /plm-repair-them-all/setup.sh

ENTRYPOINT ["cd", "/plm-repair-them-all"]