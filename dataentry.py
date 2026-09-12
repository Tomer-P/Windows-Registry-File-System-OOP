from abc import abstractmethod, ABC
from entry import Entry

class DataEntry(Entry):

    @abstractmethod
    def read_data(self): # an abstract function which returns a string of the file's data.
        print("reading data")
        return

    @abstractmethod
    def write_data(data, self): # an abstract function which changes the file's content.
        print("writing data")
        return
