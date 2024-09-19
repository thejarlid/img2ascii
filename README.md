# img2ascii

This is a command line tool which prints out a provided image in ascii to the terminal. You may have to zoom out a lot to view the printed image in your terminal 

## Setup

The python requirements can be installed using pip. 

```
# start a venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

For webcam usage we use [imagesnap](https://github.com/rharder/imagesnap). The easiest way to install imagesnap is probably with one of those commands such as `brew install imagesnap`. For more detailed setup see the [imagesnap repo](https://github.com/rharder/imagesnap).


## Usage

This tool can be configured to generate ascii art from a provided image or from your webcam on a mac. 

```
# Running with webcam
python3 main.py -c

# run with a provided image
python3 main.py -f <filename>
```

### Example
```
python3 main.py -c
```

![Example Webcam Usage](https://i.imgur.com/mg56xpg.png)
