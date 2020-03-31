#!/bin/bash


#intro
rm -fr config
#git clone gitserver://devopseliteteam/config
git clone ../config

#main
./packages.sh
#./selinux_rules.sh
#./users.sh
./terraform.sh

#outro
