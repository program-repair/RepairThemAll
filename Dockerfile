FROM java:8

# Install basic utils and build envs.
RUN apt-get update -qq
RUN apt-get install -y git
RUN apt-get install -y subversion
RUN apt-get install -y perl
RUN apt-get install -y unzip
RUN apt-get install -y libdbi-perl
RUN apt-get install -y libtext-csv-perl
RUN apt-get install -y libdbd-csv-perl
RUN apt-get install -y debconf
RUN apt-get install -y curl
RUN apt-get install -y software-properties-common
RUN apt-get install -y python
RUN apt-get install -y maven
RUN apt-get install -y patch

# install runner
RUN mkdir /results
COPY benchmarks /benchmarks
COPY script /script
COPY repair_tools /repair_tools
COPY libs /libs
COPY init.sh /init.sh 

RUN /init.sh

ENTRYPOINT [ "script/RepairThemAll.py" ] 