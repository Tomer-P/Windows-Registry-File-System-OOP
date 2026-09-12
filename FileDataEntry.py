from dataentry import DataEntry
import os.path
import os

class FileDataEntry(DataEntry):

    def __init__(self, file_name):
        self.file_name = file_name # the file's name, for example class.txt.

    def get_path(self):  # a function which returns a string of the file's path.
        if os.path.exists(self.file_name):
            path = os.path.abspath(self.file_name)
        else:
            path = 'the file does not exist'
        return str(path)

    def get_permission(self): # a function which returns a string of the users' permissions- read or write.
        string = ''
        read = os.access(self.file_name, os.R_OK)  # Check for read access
        write = os.access(self.file_name, os.W_OK)  # Check for write access
        string += "read:"+str(read)+" write:"+str(write)
        return string

    def read_data(self): #a function which returns a string of the file's data.
        path_file = self.get_path()
        name = self.get_permission().split(" ")
        if name[0] == 'read:True':
            open_file = open(path_file, "r")
            data = open_file.read()
            return data
        return ("You don't have a permission to read or write to this file")

    def write_data(self, data):  # a function which changes the file's content.
        name = self.get_permission().split(" ")
        if name[1] == "write:True":
            my_file = open(self.file_name, "w")
            my_file.write(data)
            my_file.close()
            return
