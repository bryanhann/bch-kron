#!/usr/bin/env bash


for pth in $(ls $(dirname ${BASH_SOURCE[0]})/[0-9]*); do
    source ${pth}
done

