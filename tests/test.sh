#!/bin/bash

if [ "$1" = clean ]
    then
        rm -f test-adm0-output.csv
        rm -f test-adm0-output.xlsx
        rm -f test-adm2-output.csv
        rm -f test-adm2-output.xlsx
    else
        centroid-lookup adm0 --adm0 name_0 test-adm0.csv
        centroid-lookup adm0 --adm0 name_0 test-adm0.xlsx
        centroid-lookup adm2 --adm0 name_0 --adm1 name_1 --adm2 name_2 test-adm2.csv
        centroid-lookup adm2 --adm0 name_0 --adm1 name_1 --adm2 name_2 test-adm2.xlsx
fi
