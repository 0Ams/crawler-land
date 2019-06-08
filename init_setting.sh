#bin/bash
pip install virtualenv
virtualenv hamu
if [ ! -d "momo" ] ; then
  exit;
fi
cd hamu
source hamu/bin/activate
pip install -r requirement.txt
