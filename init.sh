git submodule init;
git submodule update;
cd benchmarks/Bug-dot-jar/;
git submodule init;
git submodule update;
cd ../defects4j;
./init.sh
cd ../../

cd libs/z3
python scripts/mk_make.py --java
cd build
make
make install
cd ../../

git clone https://github.com/tdurieux/project-info-maven-plugin
cd project-info-maven-plugin 
mvn -Dhttps.protocols=TLSv1.2 install -DskipTests
cd ..
rm -rf project-info-maven-plugin