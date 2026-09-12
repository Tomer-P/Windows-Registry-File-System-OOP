import os.path
import pathlib
from entry import Entry
from os import listdir
from os.path import isfile, join


class DirectoryEntry(Entry):

    def __init__(self, dir):
        self.dir = dir # the directory's name, for example OOP_generic.

    def get_path(self): # a function which returns a string of the directory's path.
        if os.path.exists(self.dir):
            dir_path = pathlib.Path(__file__).parent.absolute()
        else:
            dir_path = 'the file does not exist'
        return str(dir_path)

    def get_permission(self): # a function which returns a string of the users' permissions- read or write.

        string = ''
        read = os.access(self.dir, os.R_OK)  # Check for read access
        write = os.access(self.dir, os.W_OK)  # Check for write access
        string += "read:"+str(read)+" write:"+str(write)
        return str(string)

    def get_all_files(self): # a function which return all the files' names in the directory.
        arr = os.listdir()
        return arr
