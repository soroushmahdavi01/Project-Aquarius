import csv
import tkinter as tk
reserved_list = {}
attended_list = {}
final_list = {}
import os, sys
def first_parse():
    with open(os.path.join(sys.path[0], 'Reserved.csv'), 'r', encoding="utf8") as reserved_file:
        reserved_reader = csv.DictReader(reserved_file)
        for line in reserved_reader:
            reserved_list[line["ID"]]=line["First Name"] + " " + line["Last Name"]
    with open(os.path.join(sys.path[0], 'Attended.csv'), 'r', encoding="utf8") as attended_file:
        attended_reader = csv.DictReader(attended_file)
        for line in attended_reader:
            attended_list[line["ID"]]=line["First Name"] + " " + line["Last Name"]
def final_parse():    
    for i in attended_list:
        if i in reserved_list:
            print(f'{attended_list[i]} r:yes a:yes')
        else:
            print(f'{attended_list[i]} r:no a:yes')
    for i in reserved_list:
        try:
            attended_list[i]
        except KeyError:
            print(f'{reserved_list[i]} r:yes a:no')
def main():
    first_parse()
    print(attended_list)
    print(reserved_list)
    final_parse()
root= tk.Tk()   
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()
year = tk.Entry (root) 
canvas1.create_window(200, 140, window=year)
button1 = tk.Button(text='Start', command=main)
canvas1.create_window(200, 180, window=button1)
root.mainloop()