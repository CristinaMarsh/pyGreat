# coding=gbk
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
l.pack()

def print_selection():
    value = lb.get('active')   # 获得光标处的值原get（lb.curselection()这个在一开始没有光标定位时会报错）.lb.get('avtive')也行，这个一开始默认光标定位在第一项
    var1.set(value)

b = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b.pack()    # 放置Button

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))  # 内容设置为元组、list都可以
lb = tk.Listbox(window, listvariable=var2)  # tk.Listbox()对象，列一列，可以往里插入值
list_items = [1, 2, 3, 4]   # 每次网上面的Listbox对象最后（end）插入一个值
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')   # 按索引插入（索引从零开始）
lb.insert(2, 'second')
lb.delete(2)
lb.pack()



window.mainloop()   # 主循环，不停地刷新？