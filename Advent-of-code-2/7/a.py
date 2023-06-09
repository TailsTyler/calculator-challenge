class Folder:
    def __init__(self, name, files, folders, parent):
        self.name = name
        self.files = files
        self.folders = folders
        self.parent = parent
        self.size = None
    def add_folder(self, folder):
        self.folders.append(folder)
    def add_file(self, file):
        self.files.append(file)





"""
    cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
    cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
    cd / switches the current directory to the outermost directory, /.
"""
def process_command_cd(string, folder_im_in):
    if string[5:7] == "..":
        if folder_im_in.parent is not None:
            folder_im_in = folder_im_in.parent
    elif string[5:6] == "/":
        folder_im_in = home
    else:
        for subfolder in range(len(folder_im_in.folders)):
            name_of_subfolder = string[5:-1:]
            if folder_im_in.folders[subfolder].name == name_of_subfolder:
                folder_im_in = folder_im_in.folders[subfolder]
                break
    return folder_im_in

def get_number_from_string(string):
    i = 0
    while i < len(string):
        if not string[i].isnumeric():
            break
        i += 1
    return int(string[0:i])

def get_folder_size(folder):
    if folder.size != None:
        return folder.size
    size = 0
    for file in folder.files:
        size += file
    for subfolder in folder.folders:
        size += get_folder_size(subfolder)
    folder.size = size
    return size

def sum_all_folders_at_most_x_big(folder, x):
    sum = 0
    if get_folder_size(folder) <= 100000:
        sum += get_folder_size(folder)
    for i in folder.folders:
        sum += sum_all_folders_at_most_x_big(i, x)
    return sum

def all_folders_at_least_x_big(folder, space_needed):
    list_of_such_folders = []
    if get_folder_size(folder) >= space_needed:
        list_of_such_folders.append(folder)
    sublist_of_such_folders = []
    for i in folder.folders:
        if get_folder_size(i) >= space_needed:
            sublist_of_such_folders.append(all_folders_at_least_x_big(i, space_needed))
    #this is so confusing... is this the best wayy?? going into [[x]] to grab x...
    for i in sublist_of_such_folders:
        for j in i:
            list_of_such_folders.append(j)
    return list_of_such_folders

def get_smallest_folder(list_of_folders):
    if type(list_of_folders[0]) != Folder:
        return None
    smallest_folder = list_of_folders[0]
    for folder in list_of_folders:
        if get_folder_size(folder) < get_folder_size(smallest_folder):
            smallest_folder = folder
    return smallest_folder



File_object = open("input", "r")
file = File_object.readlines()
# print(file)
# for i in range(len(file)):
#     print(i,': ',file[i])
home = Folder('/', [], [], None)
folder_im_in = home
for line in file:
    if line[2:4] == "cd":
        folder_im_in = process_command_cd(line, folder_im_in)
    elif line[0:3] == "dir":
        folder_im_in.folders.append(Folder(line[4:-1], [], [], folder_im_in))
    elif line[0].isnumeric():
        file_size = get_number_from_string(line)
        folder_im_in.files.append(file_size)
    else:
        pass

used_space = get_folder_size(home)

print(used_space)

print(sum_all_folders_at_most_x_big(home, 100000))

total_space_needed_for_update = 30000000
total_space = 70000000
unused_space = total_space - used_space
space_needed = total_space_needed_for_update - unused_space

all_folders_which_alone_could_provide_enough_space = all_folders_at_least_x_big(home, space_needed)
print("\nall_folders_which_alone_could_provide_enough_space:")
print(all_folders_which_alone_could_provide_enough_space)

smallest_qualifying_folder = get_smallest_folder(all_folders_which_alone_could_provide_enough_space)
print("\nsmallest_qualifying_folder's name:")
print(smallest_qualifying_folder.name)
print("\nsmallest_qualifying_folder's size:")
print(get_folder_size(smallest_qualifying_folder))











