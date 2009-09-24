#!/bin/bash

rm -rf build
mkdir build
cd build
svn co https://webarok.svn.sourceforge.net/svnroot/webarok webarok 
find . -name ".svn" -exec rm -rf {} \;
tar cjf webarok.tar.bz2 webarok
