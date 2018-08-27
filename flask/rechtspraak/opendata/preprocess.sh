#!/bin/bash


# dit is een script met wat ruwe hacks...
# use at your own peril
set -e

function fix_json_file() {
    f=$1
    echo "INFO: attempting to fix $f..."
    if (jsonlint -c $f > /dev/null) 2>&1 | grep "expected: 'STRING'" > /dev/null ; then
        LN=$((jsonlint -c $f > /dev/null) 2>&1 | awk '{ print $3 }' | sed -e 's/,//')
        echo "INFO: found jsonlint error on line $LN, attempting to fix..."
        d="${LN}s"
        sed -i "$d/,$//" $f
        RET=1
    else
        echo "INFO: found no jsonlint errors..."
        RET=0
    fi
    return $RET
}

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
#FIXME for folder in uitspraken/*/; do
for folder in uitspraken/2010/; do
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
          echo "------- $xmlfile"
          fbname=$(basename "$xmlfile" .xml)
          jsname="$fbname.json"
          xmlname="$fbname.xml"
          #echo "DEBUG: $fbname $jsname $xmlname"
          if [ ! -f $jsname ]; then
              echo "INFO: xml2json $fbname"
              python ../../xml2json.py --pretty --strip_namespace --strip_newlines -t xml2json -o $jsname $xmlname
              /usr/bin/sed -i -f ../../preprocess.sed $jsname || exit 1

              if (jsonlint -c $jsname > /dev/null) 2>&1 | grep "expected: 'STRING'" > /dev/null ; then
                  echo "INFO: found jsonlint error, attempting to fix..."
                  while ! fix_json_file "$jsname"; do
                      echo -n
                  done
              fi

              if cat $jsname | json_verify -u > /dev/null 2>&1 ; then
                  echo "INFO: valid json in $jsname"
                  echo "INFO compressing $xmlname"
                  gzip $xmlname
              else
                  echo "ERR: invalid json in $jsname"
                  mv $jsname $jsname.invalidjson
              fi
          else
              echo "INFO: skip $fbname, json allready created and checked for validity"
          fi
      done
  cd $CURRENT_PWD
done
