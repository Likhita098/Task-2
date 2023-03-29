from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('CodeClause.com - TextPad!')
root.geometry("1200x660")

#Set variable for open file name
global open_status_name
open_status_name=False

global selected
selected=False
#Create new file function
def new_file():
    my_text.delete("1.0",END)
    #update previous text
    root.title('New File - TextPad!')
    status_bar.config(text="New File        ")
    global open_status_name
    open_status_name=False


#open file function
def open_file():
    #delete previous text
    my_text.delete("1.0",END)

    #grab file name
    text_file = filedialog.askopenfilename(initialdir="",title="Open File",filetypes=(("Text Files","*.txt"), ("HTML Files","*.html"),("Python Files","*.py"),("All Files","*.*")))
    #Check to see if there is a file name
    if text_file:
       #Make file name global so we can access it later
       global open_status_name
       open_status_name=text_file
    #Update status bars
    name=text_file
    status_bar.config(text=f'{name}        ')
    root.title(f'{name} - TextPad!')

    #open the file
    text_file=open(text_file,'r')
    stuff=text_file.read()
    #Add file to textbox
    my_text.insert(END,stuff)
    #Close the opened file
    text_file.close()

#save as file
def save_as_file():
    text_file=filedialog.asksaveasfilename(defaultextension=".*",initialdir="",title="Save File",filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("Python","*.py"),("All Files","*.*")))
    if text_file:
        #Update status bar
        name=text_file
        status_bar.config(text=f'Saved:{name}        ')
        root.title(f'{name} - TextPad!')

        #Save the file
        text_file=open(text_file,'w')
        text_file.write(my_text.get(1.0,END))
        #Close the file
        text_file.close()

#save the file
def save_file():
    global open_status_name  
    if open_status_name:
        #Save the file
        text_file=open(open_status_name,'w')
        text_file.write(my_text.get(1.0,END))
        #Close the file
        text_file.close()

        status_bar.config(text=f'Saved:{open_ststus_name}        ')
    else:
        save_as_file()

#Cut text
def cut_text(e):
    global selected
    #Check to see if we used keyboard shortcuts
    if e:
        selected=root.clipboard_get()
    else:
      if my_text.selection_get():
        #Grab selected text from text box
        selected=my_text.selection_get()
        #Select selected text from text box
        my_text.delete("sel.first","sel.last")


#Copy text
def copy_text(e):
    global selected
    #Check to see if we used keyboard shortcuts
    if e:
        selected=root.clipboard_get()
    if my_text.selection_get():
        #Grab selected text from text box
        selected=my_text.selection_get()
        #clear the clipboard then append
        root.clipboard_clear()
        root.clipboard_append(selected)
#Paste text
def paste_text(e):
    global selected
    #Check to see if we used keyboard shortcuts
    if e:
        selected=root.clipboard_get()
    else:  
        if selected:
           position=my_text.index(INSERT)
           my_text.insert(position,selected)
#Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#Create our Scrollbar for the text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Create Text box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="blue", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

#Configure our Scrollbar
text_scroll.config(command=my_text.yview)

#Create Menu
my_menu= Menu(root)
root.config(menu=my_menu)

#Add file Menu
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Save As",command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

#Add edit menu
edit_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut \t\tCtrl+x",command=lambda:cut_text(False))
edit_menu.add_command(label="Copy \t\tCtrl+c",command=lambda:copy_text(False))
edit_menu.add_command(label="Paste \t\tCtrl+v",command=lambda:paste_text(False))

#Edit bindings
root.bind('<Control-Key-x>',cut_text)
root.bind('<Control-Key-c>',copy_text)
root.bind('<Control-Key-v>',paste_text)


#Add status bar to bottom of app
status_bar=Label(root,text='Ready        ',anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=5)
root.mainloop()