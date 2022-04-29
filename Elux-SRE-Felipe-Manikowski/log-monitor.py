#Developed by Felipe Manikowski

import os

def read_over (file_name, session_id):
    with open(file_name, "r") as file:
        for line in file:
            l = line.split(',')
            if session_id == l[1] and not e in l[2]:
                first_line("report.csv", str(l))

def first_line(file_name, line):
    """ Insert given string as a new line at the beginning of a file """
    dummy_file = file_name + '.bak'
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        write_obj.write("\n" + line)
        for line in read_obj:
            write_obj.write(line)
    os.remove(file_name)
    os.rename(dummy_file, file_name)


e = 'ERROR'
filelog = open('filelog.csv', 'r')
report = open('report.csv', 'w')


for line in filelog:
    l = line.split(',')
    session_id = l[1]
    if e in l[2]:
        first_line("report.csv", "-----")
        first_line("report.csv", str(l))
        read_over("filelog.csv", session_id)
    else:
        continue

filelog.close()
report.close()        