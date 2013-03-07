#!/bin/bash
#########################################################
#   Filename   : populate.sh                             #
#   Description: TODO   #
#########################################################

PROGNAME="$(basename $0)"
quiet=false
testnumber=10
hostnumber=10

hostformat="myhost"
testformat="mytest"

url="http://localhost:8080/event"


set -u
set -e

# Prints help message
function showhelp {
    cat >&2 <<- EOF 
Usage: $PROGNAME [OPTION] ...
Options:
    -h  prints this help message.
EOF
}

# Prints log message to default output
function log {
    local level="$1"
    local message="$2"

    $quiet || echo "$(date +"%F %T" ) $PROGNAME: $message" 
}

while getopts "t:H:qh" opt
do
    case $opt in
        t)  testnumber=$OPTARG
            ;;
        H)  hostnumber=$OPTARG
            ;;
        q)  quiet=true
            ;;
        h)  showhelp
            exit 1
            ;;
        *)  showhelp
            exit 1
            ;;
    esac
done

data="default"

for h in $(seq 0 $hostnumber)
do
    currenthost="$hostformat-$h.test"
    for t in $(seq 0 $testnumber)
    do
        currenttest="$testformat$t"
        timestamp="$(date +%s)"
        level="$RANDOM"
        request="reference=$currenthost&test=$currenttest&timestamp=$timestamp"
        request="$request&level=$level&data=$data"
        curl "$url?$request"
    done
done

