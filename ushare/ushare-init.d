#!/bin/sh -e
#
# uShare init script
#
### BEGIN INIT INFO
# Provides: ushare
# Required-Start: $local_fs $syslog $network
# Should-Start:
# Required-Stop:
# Should-Stop:
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: uShare
# Description: uShare UPnP (TM) A/V & DLNA Media Server
# You should edit configuration in /etc/ushare.conf file
# See http://ushare.geexbox.org for details
### END INIT INFO

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
DAEMON=/usr/bin/ushare
NAME=ushare
DESC="uShare UPnP A/V & DLNA Media Server"
PIDFILE=/var/run/ushare.pid
CONFIGFILE=/etc/ushare.conf
USHARE_OPTIONS=" --cfg $CONFIGFILE "

# abort if no executable exists
[ -x $DAEMON ] || exit 0

# Get lsb functions
. /lib/lsb/init-functions
. /etc/default/rcS

[ -f /etc/default/ushare ] && . /etc/default/ushare

checkpid() {
[ -e $PIDFILE ] || touch $PIDFILE
}

check_shares() {
return 0
if [ -r "$CONFIGFILE" ]; then
. $CONFIGFILE
[ -n "$USHARE_DIR" ] && return 0
fi
return 1
}

case "$1" in
start)
log_daemon_msg "Starting $DESC: $NAME"
if ! $(check_shares); then
log_warning_msg "No shares avalaible ..."
log_end_msg 0
else
start-stop-daemon --start --background --quiet --make-pidfile --pidfile $PIDFILE --exec $DAEMON -- $USHARE_OPTIONS
log_end_msg $?
fi
;;
stop)
log_daemon_msg "Stopping $DESC: $NAME"
start-stop-daemon --stop --quiet --pidfile $PIDFILE
log_end_msg $?
;;
reload|force-reload)
log_daemon_msg "Reloading $DESC: $NAME"
start-stop-daemon --stop --signal 1 --quiet --oknodo --pidfile $PIDFILE --exec $DAEMON
log_end_msg $?
;;
restart)
log_daemon_msg "Restarting $DESC: $NAME"
start-stop-daemon --stop --quiet --pidfile $PIDFILE
if ! $(check_shares); then
log_warning_msg "No shares avalaible ..."
log_end_msg 0
else
start-stop-daemon --start --background --quiet --make-pidfile --pidfile $PIDFILE --exec $DAEMON -- $USHARE_OPTIONS
log_end_msg $?
fi
;;
*)
N=/etc/init.d/$NAME
log_success_msg "Usage: $N {start|stop|restart|reload|force-reload}"
exit 1
;;
esac

exit 0 
