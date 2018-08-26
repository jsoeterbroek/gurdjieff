#!/bin/bash
set -e

ONETIMEZIPFILE="OpenDataUitspraken.zip"
# eenmalig, iedere maand update
mkdir -p uitspraken
if [ -f uitspraken/$ONETIMEZIPFILE ]; then
    echo "one-time only zipfile '$ONETIMEZIPFILE' allready present"
else
    cd uitspraken
    #wget http://static.rechtspraak.nl/PI/OpenDataUitspraken.zip
    cd -
fi

# assume unpacked
CURRENT_PWD_BASENAME=$(basename $(pwd))
CURRENT_PWD=$(pwd)
#for folder in uitspraken/*/; do
for folder in uitspraken/2010/; do
  #echo "------- $folder"
  cd "$folder"
      if [ -f .unzipped ]; then
          echo "nothing to unzip in ${folder%/}"
      else
          echo "unzipping in ${folder%/}"
          shopt -s nullglob
          for f in *.zip; do
              fbname=$(basename "$f" .zip)
              echo "unzipping ${file}"
              unzip -f $f > /dev/null
          done
          touch .unzipped

      fi
      for xmlfile in *.xml; do
          fbname=$(basename "$xmlfile" .xml)
          jsname="$fbname.json"
          xmlname="$fbname.xml"
          #echo "DEBUG $fbname $jsname $xmlname"
          if [ ! -f $jsname ]; then
              echo "xml2json $fbname"
              python ../../xml2json.py --pretty --strip_namespace --strip_newlines -t xml2json -o $jsname $xmlname
              /usr/bin/sed -i -f ../../preprocess.sed $jsname || exit 1
              cat $jsname | json_verify -u || mv $jsname $jsname.invalid
              echo "compressing $xmlname"
              gzip $xmlname
          else
              echo "skip $fbname"
          fi
      done
  cd $CURRENT_PWD
done
