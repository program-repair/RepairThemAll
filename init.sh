# from https://askubuntu.com/questions/916976/bash-one-liner-to-check-if-version-is
version_checker() {
    local ver1=$1
    
    while [ `echo $ver1 | egrep -c [^0123456789.]` -gt 0 ]; do
        char=`echo $ver1 | sed 's/.*\([^0123456789.]\).*/\1/'`
        char_dec=`echo -n "$char" | od -b | head -1 | awk {'print $2'}`
        ver1=`echo $ver1 | sed "s/$char/.$char_dec/g"`
    done 
  
    local ver2=$2
    while [ `echo $ver2 | egrep -c [^0123456789.]` -gt 0 ]; do
        char=`echo $ver2 | sed 's/.*\([^0123456789.]\).*/\1/'`
        char_dec=`echo -n "$char" | od -b | head -1 | awk {'print $2'}`
        ver2=`echo $ver2 | sed "s/$char/.$char_dec/g"`
    done    

    ver1=`echo $ver1 | sed 's/\.\./.0/g'`
    ver2=`echo $ver2 | sed 's/\.\./.0/g'`
    
    do_version_check "$ver1" "$ver2"
}

do_version_check() {

    [ "$1" == "$2" ] && return 10

    ver1front=`echo $1 | cut -d "." -f -1`
    ver1back=`echo $1 | cut -d "." -f 2-`
    ver2front=`echo $2 | cut -d "." -f -1`
    ver2back=`echo $2 | cut -d "." -f 2-`

    if [ "$ver1front" != "$1" ] || [ "$ver2front" != "$2" ]; then
        [ "$ver1front" -gt "$ver2front" ] && return 11
        [ "$ver1front" -lt "$ver2front" ] && return 9

        [ "$ver1front" == "$1" ] || [ -z "$ver1back" ] && ver1back=0
        [ "$ver2front" == "$2" ] || [ -z "$ver2back" ] && ver2back=0
        do_version_check "$ver1back" "$ver2back"
        return $?
    else
        [ "$1" -gt "$2" ] && return 11 || return 9
    fi
}

git submodule init;
git submodule update;
cd benchmarks/Bug-dot-jar/;
git submodule init;
git submodule update;
cd ../defects4j;
./init.sh
cd ../../

perl_version=`perl -e 'print $];'`
do_version_check "$perl_version" "5.0.10" 
[[ $? -eq 9 ]] && echo "[Error] Perl version >= 5.0.10" && exit 1 ;

which wget > /dev/null
[[ $? -eq 1 ]] && echo "[Error] wget not installed" && exit 1 ;

do_version_check "`svn --version --quiet`" "1.8" 
[[ $? -eq 9 ]] && echo "[Error] snv version >= 1.8" && exit 1 ;

version_checker "`git version | sed "s/git version //"`" "1.9" 
[[ $? -eq 9 ]] && echo "[Error] git version >= 1.9" && exit 1 ;

which gradle > /dev/null
[[ $? -eq 1 ]] && echo "[Error] gradle not installed" && exit 1 ;

which time > /dev/null
[[ $? -eq 1 ]] && echo "[Error] time not installed" && exit 1 ;

which mvn > /dev/null
[[ $? -eq 1 ]] && echo "[Error] maven not installed" && exit 1 ;

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