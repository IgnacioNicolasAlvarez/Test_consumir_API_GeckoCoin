#! /bin/bash


start_date=$(TZ=America/Buenos_Aires date -d "yesterday 23:00" '+%d-%m-%Y')
echo "start_date: $start_date"

while read coin
do
    python3 main.py "$coin" --start-date $start_date --to-db
done < coins.txt
