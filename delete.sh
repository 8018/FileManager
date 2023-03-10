#! /bin/bash

find ~/downloads/taotu8/  -type d -name '*副本*' -print0 | xargs -0  rm -rf 
find ~/downloads/taotu8/  -type d -name '*-1' -print0 | xargs -0  rm -rf 
find ~/downloads/taotu8/  -type d -name '*-2' -print0 | xargs -0  rm -rf 
find ~/downloads/taotu8/  -type f -name '*.txt' -print0 | xargs -0  rm -rf 
find ~/downloads/taotu8/  -type f -name '*.url' -print0 | xargs -0  rm -rf 
find ~/downloads/taotu8/  -type f -name '*.7z' -print0 | xargs -0  rm -rf 
find ~/downloads/taotu8/  -type f -name '*.zip' -print0 | xargs -0  rm -rf 
find ~/downloads/taotu8/  -type f -name '*.tar' -print0 | xargs -0  rm -rf 

 