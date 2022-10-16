from typing import List


class Directory:

    def __init__(self,
                 name: str,
                 root: 'Directory' = None,
                 files: List['File'] = None,
                 sub_directories: List['Directory'] = None):
        self.name = name
        self.root = root
        self.files = files if files is not None else []
        self.sub_directories = sub_directories if sub_directories is not None else []

    def add_sub_directory(self, new_dir: 'Directory'):
        self.sub_directories.append(new_dir)
        new_dir.root = self

    def remove_sub_directory(self, rem_dir: 'Directory'):
        if rem_dir in self.sub_directories:
            self.sub_directories.remove(rem_dir)
            rem_dir.root = None
        else:
            print("There isn't such a directory in the list")

    def add_file(self, new_file):
        self.files.append(new_file)
        new_file.directory = self

    def remove_file(self, rem_file):
        if rem_file in self.files:
            self.files.remove(rem_file)
            rem_file.directory = None


class File:

    def __init__(self,
                 name: str,
                 directory: 'Directory' = None):
        self.name = name
        self.directory = directory


# testing
myfile1 = File('test1.txt')
mydir1 = Directory('main folder')
mydir2 = Directory('test subfolder')
mydir1.add_sub_directory(mydir2)
mydir2.add_file(myfile1)

print(mydir2.name)
print(mydir2.root.name)
print(mydir2.files[-1].name)
