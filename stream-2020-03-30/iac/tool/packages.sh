#!/bin/bash

for package in $(cat config/data.yml | grep '-' | cut -d "-" -f 2-)
do
    echo apt-get install $package
done

