#! /bin/bash

cwd=$(pwd)

for dir in *
do
  cd dir
  for sub_dir in *
  do
    rm -rf ${sub_dir%.*}
  done
  cd $cwd
done
