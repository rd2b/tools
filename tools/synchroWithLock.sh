#!/bin/bash
#############################################################
#	Name: 	synchroWithLock.sh		 	    #
#	Description: Synchornizes data from prod to preprod #
#############################################################
#
#

set -e
set -u

quiet=false
scriptName="synchroWithLock.sh"

pidfile="/tmp/$scriptName.pid.inprogress"
facility=local1

RSYNC_DATA_LOGFILE=/var/log/$scriptname.log
RSYNCTIMEOUT=5
RSYNCSSHTIMEOUT="ssh -o ConnectTimeout=5"
RSYNCIGNORELIST=""
RSYNCTEMPDIR="/tmp"

function reportError {
        local level=$1
        local message=$2
        local pid=${3:-$$}
        local curVerbose=false

        case "$level" in
                "error")
                        curFacility="$facility.err"
                        $quiet || curVerbose=true
                        ;;
                "warn")
                        curFacility="$facility.warn"
                        $quiet || curVerbose=true
                        ;;
                "info")
                        curFacility="$facility.info"
                        $quiet || curVerbose=$verbose
                        ;;
                "debug")
                        curFacility="$facility.debug"
                        $quiet || curVerbose=$debug
                        ;;
        esac

        if [ -n "$curFacility" ]; then
                $curVerbose \
                        && logger -s -t "$scriptName[${pid:-$$}]" -p $curFacility "$level: $message" \
                        || logger -t "$scriptName[${pid:-$$}]" -p $curFacility "$level: $message"
        fi
}

function show_help {
        $quiet && exit -1
        cat >&2 <<- EOF
	Usage $0 [option]
	Synchronise datas from prod to vprod.

	Options are:
        -f, server to sync from. 
	-t, path to sync to.
	-q, quiet (no output to stdout)
	-h, display this help
	EOF

        exit -1
}

function log {
    local message="$1"
    ! $quiet && echo "$message"
}


while getopts "qhf:t:" opt; do
        case $opt in
		f)	from=$OPTARG
			;;
		t)	to=$OPTARG
			;;
                q)
                        quiet=true
                        ;;
                h)
                        show_help
                        ;;
                \?)
                        reportError "error" "Invalid option: -$OPTARG" >&2
                        show_help
                        ;;
                :)
                        reportError "error" "Option -$OPTARG requires an argument." >&2
                        show_help
                        ;;
                *)
                        reportError "error" "Invalid option: -$OPTARG" >&2
                        show_help
                        ;;
        esac
done


[[ -f $pidfile ]] && {
    reportError "error" "Le script $0 est deja lance"
    exit 1
}

echo "$$"> $pidfile

log "Starting sync from $from to $to"

if rsync -e "$RSYNCSSHTIMEOUT" \
                --timeout=$RSYNCTIMEOUT \
                --exclude $RSYNCIGNORELIST \
                --exclude "lost+found" \
                --temp-dir="$RSYNCTEMPDIR" \
                --recursive \
                --times \
                --perms \
                --links \
                --group \
                --omit-dir-times \
		--log-file=$RSYNC_DATA_LOGFILE \
                --compress $from $to  &> /dev/null
then 
    log "Synchro en succes"
else
     reportError "error" "Le rsync a rencontre une erreur $?"
     rm -f $pidfile
     exit 2
fi




rm -f $pidfile
exit 0




