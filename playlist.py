#!/usr/bin/python3
import os
class MakePlaylist:
    def __init__(self,file_name='playlist.m3u',file_type=['mp3','flac']):
        self.file_name=file_name
        self.file_type=file_type

    def makePlaylist(self):
        all_files=os.listdir()
        files=[]
        for i in all_files:
            if i.endswith(tuple(self.file_type)):
                files.append(i)
        if files:
            with open(self.file_name,'w') as player:
                player.write('\n'.join(files))

print("\tWelCome To Playlist Maker")
ft=input("You want To make a Playlist of which Files ?\nput a , to separate them (ex: mp3,flac or * ): ")
forformat=['flac','mp3','mmf','ogg','oga','mogg','au','dvf','msv','ra','rm','dss','nmf','wma','ape','opus','iklax','voc','aa','aax','aiff','alac','m4p','ivs','aac','act','amr','awb','gsm','m4a','m4b','mpc','raw','rf64','sln','tta','vox','wav','wv','webm','cda']
if ft=='*':
    file_type=forformat
elif ft=='':
    file_type = ['mp3','flac']
else:
    ftype = ft.split(',')
    file_type = [i for i in ftype if i in forformat]

make=MakePlaylist(file_type=file_type)
make.makePlaylist()
