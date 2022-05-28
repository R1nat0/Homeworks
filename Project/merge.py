"""
Module to merge
"""

def merge(path1, path2, res_path):
    """
    Merge two files
    """
    with open(res_path, 'w', encoding='utf-8') as file_rez:
        with open(path1, 'w', encoding='utf-8') as file1:
            with open(path2, 'w', encoding='utf-8') as file2:
                line1 = file1.readline()
                line2 = file2.readline()
                while True:
                    if line1 == line2 == '':
                        return
                    elif line1 == '' and line2 != '':
                        while line2 != '':
                            file_rez.write(line2)
                        return
                    elif line1 != '' and line2 == '':
                        while line1 != '':
                            file_rez.write(line1)
                        return
                    else:
                        if line1 < line2:
                            file_rez.write(line1)
                            line1 = file1.readline()
                        elif line1 > line2:
                            file_rez.write(line2)
                            line2 = file2.readline()
                        else:
                            new_count = int(line1.split(' ')[-1]) + int(line2.split(' ')[-1])
                            new_word = str(line1.split(' ')[:len(line1)])
                            new_line = new_word + ' ' + str(new_count)
                            file_rez.write(new_line)
                            line2 = file2.readline()
                            line1 = file_rez.readline()

def multi_merge(*paths, result='result.txt'):
    """
    Merge many files
    """
    result = paths[0]
    help_file = 'help.txt'
    for path in paths[1:]:
        merge(path, result, help_file)
        result = help_file

if __name__ == "__main__":
    pass
