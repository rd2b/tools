# This script is ran the first time a user logs in

echo "Your appliance is about to be finished to be set up."
echo "In order to do it, we'll need to ask you a few questions,"

#give the opportunity to change the keyboard
sudo dpkg-reconfigure console-setup

echo "starting by changing adding root password."
sudo passwd


