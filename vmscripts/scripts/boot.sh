# This script will run the first time the virtual machine boots
# It is ran as root.

apt-get update
apt-get install -qqy --force-yes openssh-server

sed -i "s/VCS=\"bzr\"/VCS=\"git\"/" /etc/etckeeper/etckeeper.conf
etckeeper init

apt-get install -qqy --force-yes glusterfs-client
sed -i "s/option\ remote-host\ 127.0.0.1/option\ remote-host\ 192\.168\.122\.101/" /etc/glusterfs/glusterfs.vol
mkdir -p /data/commun

echo "# Partage glusterfs :" >> /etc/fstab
echo "/etc/glusterfs/glusterfs.vol /data/commun  glusterfs  defaults  0  0" >> /etc/fstab
