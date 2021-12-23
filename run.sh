#! /bin/bash

echo "Running the test..."
python3 main.py $1 --start-date $2 --end-date $3
echo "Done"