#!/usr/bin/python
# -*- coding: utf-8 -*-
# DirectoryTree Running in Python 3.3.0

import os
import time
import tkinter
from tkinter import messagebox

class NoteForFileCatalog(tkinter.Tk):

    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title('Note in Catalog')
        self.minsize(150,25)
        self.maxsize(1150,25)
        self.wm_state('zoomed')
        
        self.root=tkinter.Frame(self)
        self.root.pack(expand='YES',fill='both')
        self.root.rowconfigure(0,weight=1)
        self.root.columnconfigure(1,weight=1)

        self.P=tkinter.Label(self.root, text='Path')
        self.P.grid(row=0,column=0)

        self.e=tkinter.StringVar()    
        self.E=tkinter.Entry(self.root,textvariable=self.e)
        self.E.grid(row=0,column=1, sticky=('e','s','w','n'), padx=1)
        self.E.rowconfigure(0,weight=10)
        self.E.columnconfigure(0,weight=1)

        self.B=tkinter.Button(self.root,text='Go', command=self.note)
        self.B.grid(row=0,column=2)
        self.B.rowconfigure(0,weight=1)

    def dirhistory(self, path):
        '''在指定目录下生成目录树文件，以便对目录各项进行备注。

        注：目录树文件中的备注仅限于单行备注。
        '''

        #首先读取旧目录文件，生成备注字典
        try:
            f = open(os.path.join(path,"Notes of "+os.path.basename(path) + ".txt"), 'r',encoding='utf-8')
        except:
            f = open(os.path.join(path,"Notes of "+os.path.basename(path) + ".txt"), 'w+',encoding='utf-8')

        c=f.read()   
        noteDict={}
        if c:
            cList=c.split('\n')
            key=''
            for cKey in cList:
                key = cKey.split('|')[0].strip()
                value = cKey.split('|')[-1].strip()
                if key not in noteDict.keys():
                    noteDict[key]=value
        f.close()
    
        #写入新目录
        f = open(os.path.join(path,'Notes of '+os.path.basename(path)+'.txt'),'w', encoding='utf-8')
        f.write('\n--------------------| '+time.strftime('%Y-%m-%d    %H:%M', time.localtime())+' |--------------------')
        catalog=os.walk(path)
        position=len(path.split('\\'))
        filecounts=0
        for i in catalog:
            dirname=i[0].split('\\')
            f.write('\n'+(len(dirname)-position)*'        '+'\\  '+dirname[-1].encode('utf-8').decode('utf-8'))
            if i[2]:
                for ii in i[2]:
                    if ii in noteDict.keys():
                        f.write('\n'+(len(dirname)-position+1)*'        '+ii.encode('utf-8').decode('utf-8')+'        |  '+noteDict[ii])
                    else:
                        f.write('\n'+(len(dirname)-position+1)*'        '+ii.encode('utf-8').decode('utf-8')+'        |  ')
                f.write('\n')
                filecounts+=len(i[2])
        f.write('\n--------------------| 总共有 '+str(filecounts)+' 个文件 |--------------------')
        f.write(c)
        f.close()

    def note(self):
        self.path=self.E.get()
        path=self.path
        if os.path.isdir(path):
            self.dirhistory(path)
            os.startfile(path)
            os.startfile(os.path.join(path,'Notes of '+os.path.basename(path)+'.txt'))
            self.destroy()
        else:
            messagebox.showwarning('Path Error'.upper(), 'The path input is wrong.'.upper())

def main():
    u=NoteForFileCatalog()
    u.mainloop()

if __name__=='__main__':
    main()
