#!/bin/bash

if [ $# -lt 2 ] ; then
	echo "usage py22bin.sh [module_1] [module_2] .. [module_n] app.py"
	exit 1
fi

APP=${@: -1}
APP=${APP%%.*}
TMP=`mktemp -u | tr '.' '_'`
python2 bundler.py $@ > $TMP.py
cython -2 -D $TMP.py --embed -o $TMP.c
gcc $(pkg-config --libs --cflags python-2.7) $TMP.c -o ${APP}
rm $TMP.c
rm $TMP.py

