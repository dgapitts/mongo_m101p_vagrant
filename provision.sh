#! /bin/bash
if [ ! -f /home/vagrant/already-installed-flag ]
then
  echo "ADD EXTRA ALIAS VIA .bashrc"
  cat /vagrant/bashrc.append.txt >> /home/vagrant/.bashrc
  echo "GENERAL APT-GET UPDATE"
  apt-get -qq update
  echo "INSTALL GIT"
  apt-get -qq -y install git
  echo "INSTALL VIM"
  apt-get -qq -y install vim
  echo "INSTALL TREE"
  apt-get -qq -y install tree
  echo "INSTALL UNZIP"
  apt-get -qq -y install unzip curl 

  apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
  echo "deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen" | tee -a /etc/apt/sources.list.d/10gen.list
  apt-get -y update
  apt-get -y install mongodb-10gen
  apt-get -y install build-essential python-dev
  apt-get -y install python-setuptools
  easy_install pymongo bottle

  touch /home/vagrant/already-installed-flag
  echo "Done!"
else
  echo "already installed flag set : /home/vagrant/already-installed-flag"
fi

