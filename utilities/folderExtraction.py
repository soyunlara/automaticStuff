import os
import re
import shutil

#Just move the pattern to match your folder names.
patron = re.compile("[Fairy Tail]v")

basepath = 'E:/Descargas'
finalpath = 'E:/Descargas/Fairy Tail Manga'

with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir() and patron.search(entry.name):
            #print('Foler name: '+entry.name)
            with os.scandir(basepath+'/'+entry.name) as content:
                for files in content:
                    print(files.name + '- Recognized. Moved.')   
                    #shutil.move(basepath+'/'+entry.name+'/'+files.name, finalpath)   