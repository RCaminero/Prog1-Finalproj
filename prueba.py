
from tkinter import *

root = Tk()
root.title("Steam Trader")
root.minsize(500, 800)
root.maxsize(500, 0)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=None)
filemenu.add_command(label="Save", command=None)
menubar.add_cascade(label="File", menu=filemenu)

root.config(bg='#2A2C2B', menu=menubar)
root.mainloop()

>> And I want to change the menu color, is it possible?
>>
>> [image: Inline image 1]
>>
>> _______________________________________________
>> Tkinter-discuss mailing list
>> Tkin...@python.org
>> https://mail.python.org/mailman/listinfo/tkinter-discuss
>>
>>
> Hello, yes it is posible:
>
> from tkinter import *
>
> root = Tk()
> root.title("Steam Trader")
> root.minsize(500, 800)
> root.maxsize(500, 0)
>
> menubar = Menu(root, background='#000099', foreground='white',
>                activebackground='#004c99', activeforeground='white')
> filemenu = Menu(menubar, tearoff=0, background='#000099',
> foreground='white',
>                 activebackground='#004c99', activeforeground='white')
> filemenu.add_command(label="Open", command=None)
> filemenu.add_command(label="Save", command=None)
> menubar.add_cascade(label="File", menu=filemenu)
>
> root.config(bg='#2A2C2B', menu=menubar)
> root.mainloop()