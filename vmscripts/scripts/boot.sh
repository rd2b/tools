# This script will run the first time the virtual machine boots
# It is ran as root.

apt-get update
apt-get install -qqy --force-yes openssh-server

