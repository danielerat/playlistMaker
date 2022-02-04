# Introduction
A Simple Python To Make A plylist Anywhere You Want (OS: LINUX)


## Setup 
------------
### To Make The Program Run Everywhere

#### Step1 : Create A folder which will hold the program (In our case , playlist.py) Anywhere you want 

##### Let's Create It In home/devPrograms
```shell
> sudo mkdir /home/devPrograms
```

##### Copy the playlist.py to the devPrograms
```shell
cp playlist.py /home/devPrograms
```

#### Step2: Add The playlist.py to the $PATH Variable
###### OPEN .bashrcfile
```shell
# Open the .bashrc file
sudo nano ~/.bashrc   
```

###### Adding Our folder in home to the path
```shell
# Write this anywehre you want then save and exit bashr
export PATH=$PATH:/home/devPrograms
```
```shell
# Finally Type this then close your terminal and open it again 
source ~/.bashrc
```

##### To Run our file simply type playlist.py

```shell
playlist.py
```