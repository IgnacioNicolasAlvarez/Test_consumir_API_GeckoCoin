#! /bin/bash

start_date=$(date -d "yesterday 13:00" '+%d-%m-%Y')
echo "start_date: $start_date"

while read coin
do
    python3 main.py "$coin" --start-date $start_date 
done < coins.txt
