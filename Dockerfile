FROM tdurieux/astor

RUN apt-get install -y time
RUN add-apt-repository ppa:openjdk-r/ppa
RUN apt-get install -y software-properties-common
RUN apt-get -o Acquire::Check-Valid-Until=false update; exit 0
RUN apt-get install --fix-missing -y -f --force-yes openjdk-7-jdk

RUN echo "deb [check-valid-until=no] http://cdn-fastly.deb.debian.org/debian jessie main" > /etc/apt/sources.list.d/jessie.list
RUN sed -i '/deb http:\/\/deb.debian.org\/debian jessie-updates main/d' /etc/apt/sources.list
RUN echo "deb http://ftp.us.debian.org/debian unstable main contrib non-free" >> /etc/apt/sources.list.d/unstable.list

RUN apt-get -o Acquire::Check-Valid-Until=false update; exit 0
RUN apt-get install --fix-missing -y --force-yes -f build-essential

# install runner
COPY .git /.git
COPY repair_tools /repair_tools
COPY libs /libs
RUN rm -rf libs/z3/build
COPY data /data
COPY init.sh /init.sh 
COPY benchmarks /benchmarks
COPY script /script

RUN /init.sh
ENTRYPOINT [ "script/repair.py" ]