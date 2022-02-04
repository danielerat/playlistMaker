# Introduction
A Simple Python To Make A plylist Anywhere You Want (OS: LINUX)


## Setup 
------------
### To Make The Program Run Everywhere

#### Step1 : Create A folder which will hold the program (In our case , playlist.py) Anywhere you want 

##### Let's Create It In home/devPrograms
```shell
sudo mkdir /home/devPrograms
```

##### Copy the playlist.py to the devPrograms
```shell
cp playlist.py /home/devPrograms
```

#### Step2: Add The playlist.py to the $PATH Variable
###### OPEN .bashrc file (Located in ~/.bashrc) with nano editor 
```shell
sudo nano ~/.bashrc   
```

###### Adding Our folder in home to the path<br>Write this anywehre you want then save and exit bashr

```shell
export PATH=$PATH:/home/devPrograms
```
###### Finally Type this then close your terminal and open it again 
```shell
source ~/.bashrc
```

##### To Run our file simply type playlist.py
```shell
playlist.py
```


## Author
Username: danielerat</br>
Names: Ilunga Gisa Daniel</br>
email:danielilunga35@gmail.com

## License
MIT
