# This script will run the first time the virtual machine boots
# It is ran as root.

apt-get update
apt-get install -qqy --force-yes openssh-server

sed -i "s/VCS=\"bzr\"/VCS=\"git\"/" /etc/etckeeper/etckeeper.conf
etckeeper init

apt-get install -qqy --force-yes glusterfs-client
mkdir -p /data/commun

echo "# Partage glusterfs :" >> /etc/fstab
echo "vm01.acgform.local:/COMMUN /data/commun glusterfs defaults 0 0" >> /etc/fstab

