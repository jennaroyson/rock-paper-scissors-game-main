#READ.md for 

## ROCK-PAPER-SCISSORS GAME

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/jennaroyson/rock-paper-scissors-game.git) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):


## Activation

After cloning the repo, navigate there from the command-line:
```
cd ~/Desktop/rock-paper-scissors-main
```

>NOTE: if "no such file exists" pops up, perhpas your repo is not on Desktop. That is okay, you can figure out the file path on your computer and use the cd function to locate adn open it (whether it is in downloads or any other location). 

>If you use terminal, you also could go to GitHub Desktop select "Repository" at the top, then "Open in Terminal" to load the environment an alternative way.


Use "pwd" function to check that your present working desktop is "rock-paper-scissors-main"


Once in the game file, use Anaconda to activate the virtual environment.
On the command line type:

```
conda create -n my-game-env python=3.8
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).

Simply type "y" to the "proceed([y]/n)?" prompt. Once the packages are installed activate your game environment with the following command:

```
conda activate my-game-env
```

## Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired player name (then make sure to SAVE the ".env" file aftwards):

    PLAYER_NAME="(Type your player name)"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [".gitignore"](/.gitignore) file). This means we need to instruct each person who uses our code needs to create their own local ".env" file.

## Usage

Now we are able to rn the game adn run the Python script. On the command line, type:

```
python game.py
```

> or python ____.py for whatever you saved your game file as, then your file will start running and promt the user for an input

>NOTE: make sure you read the requirements.txt file and install the necessary packages if any issues arise.

Now lets play!

