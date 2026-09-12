from DirectoryEntry import DirectoryEntry
import os.path
import os
import winreg
from winreg import *

class RegistryDirectoryEntry(DirectoryEntry):

    def __init__(self, dirName):
        self.dirName = dirName # the directory's name, for example New_Key.

    def get_path(self): # a function which returns a string of the directory's path.
        if (winreg.OpenKey(winreg.HKEY_CURRENT_USER,self.dirName)):
            return self.dirName
        return "the file does not exist"

    def get_permission(self): # a function which returns a string of the users' permissions- read or write.
        string = ''
        if (winreg.OpenKey(winreg.HKEY_CURRENT_USER,self.dirName,access=winreg.KEY_READ)):
            read = True
        else:
            read = False

        if (winreg.OpenKey(winreg.HKEY_CURRENT_USER,self.dirName,access=winreg.KEY_WRITE)):
            write = True
        else:
            write = False
        string += "read:"+str(read)+" write:"+str(write)
        return string

    def get_all_files(self): # a function which return all the files' names in the directory.
        parentKey = winreg.OpenKey(HKEY_CURRENT_USER, self.dirName)
        i = 0
        string = ''
        while True:
            try:
                key = winreg.EnumKey(parentKey, i)
                string+=key+'\n'
                i += 1
            except WindowsError:
                return string

    def display(self, s): # a function which print all the files' names in the directory.
        print('\nfiles in '+self.dirName+':')
        print(s)
