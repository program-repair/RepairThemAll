git submodule init;
git submodule update;
cd benchmarks/Bug-dot-jar/;
git submodule init;
git submodule update;
cd ../defects4j;
./init.sh
cd ../../

mvn org.apache.maven.plugins:maven-dependency-plugin:3.1.1:get -DremoteRepositories=https://tdurieux.github.io/maven-repository/snapshots/ -Dartifact=com.github.tdurieux:project-config-maven-plugin:1.0-SNAPSHOT;