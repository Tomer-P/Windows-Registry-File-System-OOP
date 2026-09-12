from DirectoryEntry import DirectoryEntry
#from filedirectoryentry import FileDirectoryEntry
from FileDataEntry import FileDataEntry
from registrydataentry import RegistryDataEntry
from registrydirectoryentry import RegistryDirectoryEntry
import random

DATA_TEXT = ['Sample registry value', 'Registry entry updated', 'Testing read/write operations', 'Operating systems project']

# Test directory
#directory = input("Enter directory path (e.g. C:/Users/user/PycharmProjects/OOP_generic): ")
directory = "C:/Users/user/PycharmProjects/OOP_generic"
print (f'dealing with directory {directory}'+'\n'+60*'-')
directory = DirectoryEntry(directory)
print ('Directory path: ' + directory.get_path())
print ('Directory permissions: ' + directory.get_permission())
for file in directory.get_all_files():
    print (file)

# Test files in directory
my_file=FileDataEntry('class.txt')
#print (f'\ndealing with file {my_file.file}'+'\n'+30*'-')
print('File path: ' + my_file.get_path())
print ('File permissions: ' + my_file.get_permission())
print('class.txt read data: ' + my_file.read_data())
my_file.write_data (DATA_TEXT[random.randint(0,3)])
print('class.txt read data after write: ' + my_file.read_data())

# Test registry data entry
registry_data=RegistryDataEntry(r'Software\Microsoft\Internet Explorer\Main')
print ('\ndealing with registery file {registry_data.key} '+'\n'+80*'-')
print('Registry path: ' + registry_data.get_path())
print('Registry permission: ' + str(registry_data.get_permission()))
print('Registry data: ' + registry_data.read_data())
registry_data.write_data (DATA_TEXT[random.randint(0,3)])
print('Registry data after update: ' + registry_data.read_data())

# test registry directory
registry_directory = RegistryDirectoryEntry(r'Software\Microsoft\Internet Explorer\Main')
print (f'\ndealing with registery directory {registry_directory.dirName}'+'\n'+80*'-')
print('Registry directory path: ' + registry_directory.get_path())
print('Registry directory permission: ' + str(registry_directory.get_permission()))
registry_directory.display(registry_directory.get_all_files())
