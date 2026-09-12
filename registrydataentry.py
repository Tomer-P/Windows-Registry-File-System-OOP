from dataentry import DataEntry
import os.path
import os
import winreg
from winreg import *


"""instruction:
    firstly, you need to create a new directory in HKEY_CURRENT_USER - New_Key.
    secondly, you need to write on the default reg file a word or sentence.
    after doing that you may run the project."""
class RegistryDataEntry(DataEntry):

    def __init__(self, file):
        self.file = file # the file's name.

    def get_path(self):  # a function which returns a string of the file's path.
        if (winreg.OpenKey(winreg.HKEY_CURRENT_USER,self.file)):
            return self.file + "\\New_Key"
        return "the file does not exist"


    def get_permission(self):  # a function which returns a string of the users' permissions- read or write.
        string = ''
        if (winreg.OpenKey(winreg.HKEY_CURRENT_USER,self.file,access=winreg.KEY_READ)):
            read = True
        else:
            read = False

        if (winreg.OpenKey(winreg.HKEY_CURRENT_USER,self.file,access=winreg.KEY_WRITE)):
            write = True
        else:
            write = False
        string += "read:"+str(read)+" write:"+str(write)
        return string

    def read_data(self): #a function which returns a string of the file's data.
        path_file = self.get_path()
        name = self.get_permission().split(" ")
        if name[0] == 'read:True':
            data = winreg.QueryValue(winreg.HKEY_CURRENT_USER,path_file)
            return str(data)
        return ("You don't have a permission to read or write to this file")

    def write_data(self, data): # a function which changes the file's content.
        path_file = self.get_path()
        name = self.get_permission().split(" ")
        if name[1] == "write:True":
            winreg.SetValue(winreg.HKEY_CURRENT_USER, path_file,REG_SZ,data)
            return
