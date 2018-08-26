#!/bin/sh

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
for folder in uitspraken/*/; do
  cd "${folder%/}"
      if [ -f .unzipped ]; then
          echo "nothing to unzip in ${folder%/}"
      else
          echo "unzipping in ${folder%/}"
          for file in *.zip; do
              echo "unzipping ${file}"
              unzip -f $file > /dev/null

              for xmlfile in *.xml; do
                  fbname=$(basename "$xmlfile" .xml)
                  jsname="$fbname.json"
                  xmlname="$fbname.xml"
                  #echo "DEBUG $fbname $jsname $xmlname"
                  if [ ! -f $jsname ]; then
                      echo "xml2json $xmlfile"
                      python ../../xml2json.py --pretty --strip_namespace --strip_newlines -t xml2json -o $jsname $xmlname
                  fi
                  touch $jsname
              done

          done
          touch .unzipped
      fi
  cd -
done
