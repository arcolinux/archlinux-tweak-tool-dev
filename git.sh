#!/bin/bash
#set -e
##################################################################################################################
# Author 	: 	Erik Dubois
# Website 	: 	https://www.erikdubois.be
# Website	:	https://www.arcolinux.info
# Website	:	https://www.arcolinux.com
# Website	:	https://www.arcolinuxd.com
# Website	:	https://www.arcolinuxforum.com
##################################################################################################################
#
#   DO NOT JUST RUN THIS. EXAMINE AND JUDGE. RUN AT YOUR OWN RISK.
#
##################################################################################################################

# checking if I have the latest files from github
echo "Checking for newer files online first"
git pull

echo "get the pacman.conf from ArchLinux"
workdir=$(pwd)
wget https://gitlab.archlinux.org/archlinux/archiso/-/raw/master/configs/releng/pacman.conf -O $workdir/usr/share/archlinux-tweak-tool/data/arch/pacman/pacman.conf

echo "get the pacman.conf from ArcoLinux"
workdir=$(pwd)
wget https://raw.githubusercontent.com/arcolinux/arcolinuxl-iso/master/archiso/airootfs/etc/pacman.conf -O $workdir/usr/share/archlinux-tweak-tool/data/arco/pacman/pacman.conf

echo "get the pacman.conf from EOS"
workdir=$(pwd)
wget https://raw.githubusercontent.com/endeavouros-team/EndeavourOS-ISO/main/airootfs/etc/pacman.conf -O $workdir/usr/share/archlinux-tweak-tool/data/eos/pacman/pacman.conf

echo "get the pacman.conf from EOS"
workdir=$(pwd)
wget https://gitlab.com/garuda-linux/tools/garuda-tools/-/raw/master/data/pacman-multilib.conf -O $workdir/usr/share/archlinux-tweak-tool/data/garuda/pacman/pacman.conf

# Below command will backup everything inside the project folder
git add --all .

# Give a comment to the commit if you want
echo "####################################"
echo "Write your commit comment!"
echo "####################################"

read input

# Committing to the local repository with a message containing the time details and commit text

git commit -m "$input"

# Push the local files to github

git push -u origin master


echo "################################################################"
echo "###################    Git Push Done      ######################"
echo "################################################################"
