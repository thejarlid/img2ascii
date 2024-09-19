# img2ascii

This is a command line tool which prints out a provided image in ascii to the terminal. You may have to zoom out a lot to view the printed image in your terminal 

## Setup

```
# start a venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

This tool can be configured to generate ascii art from a provided image or from your webcam on a mac. 

```
# Running with webcam
python3 main.py -c

# run with a provided image
python3 main.py -f <filename>
```
