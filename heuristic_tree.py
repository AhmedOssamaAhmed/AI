from tkinter import *
from tkinter import ttk

def tree(frame,lst = [(1,'no nodes',''),]):
    style= ttk.Style()
    style.theme_use('clam')

    tree= ttk.Treeview(frame, column=("c1", "c2",), show='headings', height= 16, selectmode="extended",)
    tree.column("#1", anchor=CENTER,minwidth=0, width=100, stretch=NO)
    tree.heading("#1", text="Node")
    tree.column("#2", anchor=CENTER,minwidth=0, width=100, stretch=NO)
    tree.heading("#2", text="h(g)")
    total_rows = len(lst)
    print(lst)
    # total_columns = len(lst[0])
    for i  in range(total_rows):
        tree.insert('', 'end', text= "0",values=(lst[i][0], lst[i][1],))

    treeScroll = ttk.Scrollbar(frame)
    treeScroll.configure(command=tree.yview)
    tree.configure(yscrollcommand=treeScroll.set)
    treeScroll.pack(side= RIGHT, fill= BOTH)
    tree.pack(expand=YES)

