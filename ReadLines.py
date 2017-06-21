__author__ = '461056'
############################################################################################
#  Purpose: To get number of lines in a code
#  Features: Reads files from given directory and prints the number of lines on the window
#            Also saves output in a .CSV file
#  Edits :   Added bg image + Subdir search + out file entry field + Clear field
############################################################################################

from tkinter import *
import os
from shutil import copyfile


def window_set():
    win.wm_title("Line Counter")        # Gives title to window
    # Set window icon
    icon = PhotoImage(file=r"C:\Drives_kp\Learning\PyCodes\LOC\icon.png")
    win.tk.call('wm', 'iconphoto', win._w, icon)
    # win.iconbitmap(r'D:\kp\avenir\images\icon2.png')
    # win.minsize(width=320, height=250)
    win.geometry("600x300") # Setting window default size
    # --- Adding Background image ---
    background_label = Label(win, image=background_image, justify=RIGHT)
    # background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


def read_data():
    get_dir = loc_entry.get('1.0', 'end-1c')
    # out_file = "LOC_File.txt"
    out_file_temp = op_fil_entry.get('1.0', 'end-1c')
    out_file = out_file_temp+".txt"
    fo = open(out_file, "a")
    fo.write("Sl.No,File Name,LOC,Path\n")
    i = 1
    for dirpath, dirnames, filenames in os.walk(get_dir):
        for filename in filenames:
            FullFile = os.path.join(dirpath, filename)  # Got file here
            DirPath = os.path.join(dirpath)
            FileName = os.path.join(filename)
            with open(FullFile) as fil:
                count_lines = len(fil.readlines())
                fo.write("%s,%s,%s,%s\n" % (i, FileName, count_lines, DirPath))
                i=i+1
    fo.close()
    csv_file = out_file_temp+".csv"
    copyfile(out_file, csv_file)
    op_text.insert(END, ("\n Number of Files Checked: %s" % (i-1)))
    op_text.insert(END, ("\n Output files available at: %s" % os.getcwd()))
    op_text.insert(END, ("\n Data Files: \n  %s\n  %s\n" % (out_file, csv_file)))


def clear_field():
    loc_entry.delete('1.0', END)
    op_fil_entry.delete('1.0', END)
    op_text.delete('1.0', END)


if __name__ == '__main__':
    win = Tk()
    background_image = PhotoImage(file=r"C:\Drives_kp\Learning\PyCodes\LOC\FileExpo.png")
    window_set()
    text_font, text_size, bg_color = "Calibri", 12, '#1E3C5C'
    # Labels and Fields
    loc = Label(win, text="Location")   # label.config(font=("Courier", 44))
    loc.config(font=(text_font, text_size), bg=bg_color, fg='white')
    loc_entry = Text(win, bd=4, height=1.2, width=43, font=(text_font, text_size), state=NORMAL)
    op = Label(win, text="Output", font=(text_font, text_size), bg=bg_color, fg='white')
    op_text = Text(win, bd=4, height=7, width=43, font=(text_font, text_size), state=NORMAL)
    op_fil = Label(win, text="Output File Name", font=(text_font, text_size), bg=bg_color, fg='white')
    op_fil_entry = Text(win, bd=4, height=1.2, width=43, font=(text_font, text_size), state=NORMAL)
    # Placement for the fields
    loc.grid(row=1, column=1, padx=7, pady=7, sticky="W")  # If it is grid it should br grid in all places
    loc_entry.grid(row=1, column=2, padx=5, pady=7)
    op_fil.grid(row=2, column=1, padx=5, pady=7)
    op_fil_entry.grid(row=2, column=2, padx=5, pady=7)
    op.grid(row=3, column=1, padx=7, pady=7, sticky="NW")  # sticky=NorthWest
    op_text.grid(row=3, column=2, padx=5, pady=5)
    # Buttons
    # q1 = Button(win, text='Close', command=win.quit, width=10, font=(text_font, text_size))
    q1 = Button(win, text='Clear', command=clear_field, width=10, font=(text_font, text_size))
    sub = Button(win, text='Submit', command=read_data, width=10, font=(text_font, text_size), relief="raised")
    sub.place(x=180, y=250)
    q1.place(x=300, y=250)
    center(win)
    win.mainloop()