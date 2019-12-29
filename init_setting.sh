#bin/bash
pip3 install virtualenv
virtualenv hamu
if [ ! -d "momo" ] ; then
  exit;
fi
cd hamu
source hamu/bin/activate
pip3 install -r requirement.txt
