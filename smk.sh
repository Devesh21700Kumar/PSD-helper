#!/bin/bash
 
dir=/var/www/smk/mypaste/psd/
# do the work
while true
do
rm pb.json strings.json
echo Running script at @  `date`
python3 scraper.py
if [ -f pb.json ]; then
python3 json_to_csv.py list pb.json $dir/partialpsd.csv
echo "Processed pb.json"
else
echo "Failed to generate pb.json"
fi
if [ -f strings.json ]; then
python3 skill.py
python3 json_to_csv.py list strings.json $dir/fullpsd.csv
echo "Processed strings.json"
else
echo "Failed to generate strings.json"
fi
echo "Sleeping ..."
sleep 2400
echo "Waking up ..."
done
exit 0 
