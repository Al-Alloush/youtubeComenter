#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Sep 20, 2019 06:09:22 PM CEST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import main_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    main_support.set_Tk_var()
    top = Toplevel1 (root)
    main_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    main_support.set_Tk_var()
    top = Toplevel1 (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1360x631+264+115")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame_OAuth = tk.Frame(top)
        self.Frame_OAuth.place(relx=0.007, rely=0.063, relheight=0.151
                , relwidth=0.283)
        self.Frame_OAuth.configure(relief='groove')
        self.Frame_OAuth.configure(borderwidth="2")
        self.Frame_OAuth.configure(relief="groove")
        self.Frame_OAuth.configure(background="#d9d9d9")
        self.Frame_OAuth.configure(highlightbackground="#d9d9d9")
        self.Frame_OAuth.configure(highlightcolor="black")

        self.Btn_OAuth = tk.Button(self.Frame_OAuth)
        self.Btn_OAuth.place(relx=0.052, rely=0.105, height=74, width=207)
        self.Btn_OAuth.configure(activebackground="#ececec")
        self.Btn_OAuth.configure(activeforeground="#000000")
        self.Btn_OAuth.configure(background="#d8882d")
        self.Btn_OAuth.configure(disabledforeground="#a3a3a3")
        self.Btn_OAuth.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Btn_OAuth.configure(foreground="#000000")
        self.Btn_OAuth.configure(highlightbackground="#d9d9d9")
        self.Btn_OAuth.configure(highlightcolor="black")
        self.Btn_OAuth.configure(pady="0")
        self.Btn_OAuth.configure(text='''Start Google OAuth 2.0''')

        self.Label_OAuth = tk.Label(self.Frame_OAuth)
        self.Label_OAuth.place(relx=0.597, rely=0.105, height=71, width=144)
        self.Label_OAuth.configure(activebackground="#f9f9f9")
        self.Label_OAuth.configure(activeforeground="black")
        self.Label_OAuth.configure(background="#d9d9d9")
        self.Label_OAuth.configure(disabledforeground="#a3a3a3")
        self.Label_OAuth.configure(foreground="#000000")
        self.Label_OAuth.configure(highlightbackground="#d9d9d9")
        self.Label_OAuth.configure(highlightcolor="black")

        self.Frame_Data = tk.Frame(top)
        self.Frame_Data.place(relx=0.294, rely=0.016, relheight=0.198
                , relwidth=0.254)
        self.Frame_Data.configure(relief='groove')
        self.Frame_Data.configure(borderwidth="2")
        self.Frame_Data.configure(relief="groove")
        self.Frame_Data.configure(background="#d9d9d9")
        self.Frame_Data.configure(highlightbackground="#d9d9d9")
        self.Frame_Data.configure(highlightcolor="black")

        self.Text_kw_1 = tk.Text(self.Frame_Data)
        self.Text_kw_1.place(relx=0.522, rely=0.16, relheight=0.192
                , relwidth=0.417)
        self.Text_kw_1.configure(background="white")
        self.Text_kw_1.configure(font="TkTextFont")
        self.Text_kw_1.configure(foreground="black")
        self.Text_kw_1.configure(highlightbackground="#d9d9d9")
        self.Text_kw_1.configure(highlightcolor="black")
        self.Text_kw_1.configure(insertbackground="black")
        self.Text_kw_1.configure(selectbackground="#c4c4c4")
        self.Text_kw_1.configure(selectforeground="black")
        self.Text_kw_1.configure(wrap="word")

        self.Text_kw_2_and_3 = tk.Text(self.Frame_Data)
        self.Text_kw_2_and_3.place(relx=0.029, rely=0.48, relheight=0.192
                , relwidth=0.388)
        self.Text_kw_2_and_3.configure(background="white")
        self.Text_kw_2_and_3.configure(font="TkTextFont")
        self.Text_kw_2_and_3.configure(foreground="black")
        self.Text_kw_2_and_3.configure(highlightbackground="#d9d9d9")
        self.Text_kw_2_and_3.configure(highlightcolor="black")
        self.Text_kw_2_and_3.configure(insertbackground="black")
        self.Text_kw_2_and_3.configure(selectbackground="#c4c4c4")
        self.Text_kw_2_and_3.configure(selectforeground="black")
        self.Text_kw_2_and_3.configure(wrap="word")

        self.Text_kw_3_and_2 = tk.Text(self.Frame_Data)
        self.Text_kw_3_and_2.place(relx=0.522, rely=0.48, relheight=0.192
                , relwidth=0.417)
        self.Text_kw_3_and_2.configure(background="white")
        self.Text_kw_3_and_2.configure(font="TkTextFont")
        self.Text_kw_3_and_2.configure(foreground="black")
        self.Text_kw_3_and_2.configure(highlightbackground="#d9d9d9")
        self.Text_kw_3_and_2.configure(highlightcolor="black")
        self.Text_kw_3_and_2.configure(insertbackground="black")
        self.Text_kw_3_and_2.configure(selectbackground="#c4c4c4")
        self.Text_kw_3_and_2.configure(selectforeground="black")
        self.Text_kw_3_and_2.configure(wrap="word")

        self.Text_kw_4_or_5 = tk.Text(self.Frame_Data)
        self.Text_kw_4_or_5.place(relx=0.029, rely=0.72, relheight=0.192
                , relwidth=0.388)
        self.Text_kw_4_or_5.configure(background="white")
        self.Text_kw_4_or_5.configure(font="TkTextFont")
        self.Text_kw_4_or_5.configure(foreground="black")
        self.Text_kw_4_or_5.configure(highlightbackground="#d9d9d9")
        self.Text_kw_4_or_5.configure(highlightcolor="black")
        self.Text_kw_4_or_5.configure(insertbackground="black")
        self.Text_kw_4_or_5.configure(selectbackground="#c4c4c4")
        self.Text_kw_4_or_5.configure(selectforeground="black")
        self.Text_kw_4_or_5.configure(wrap="word")

        self.Label4 = tk.Label(self.Frame_Data)
        self.Label4.place(relx=0.058, rely=0.08, height=21, width=92)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Every Keyword''')

        self.Label4_3 = tk.Label(self.Frame_Data)
        self.Label4_3.place(relx=0.029, rely=0.24, height=21, width=102)
        self.Label4_3.configure(activebackground="#f9f9f9")
        self.Label4_3.configure(activeforeground="black")
        self.Label4_3.configure(background="#d9d9d9")
        self.Label4_3.configure(disabledforeground="#a3a3a3")
        self.Label4_3.configure(foreground="#000000")
        self.Label4_3.configure(highlightbackground="#d9d9d9")
        self.Label4_3.configure(highlightcolor="black")
        self.Label4_3.configure(text='''in Text Label''')

        self.Text_kw_5_or_4 = tk.Text(self.Frame_Data)
        self.Text_kw_5_or_4.place(relx=0.522, rely=0.72, relheight=0.192
                , relwidth=0.417)
        self.Text_kw_5_or_4.configure(background="white")
        self.Text_kw_5_or_4.configure(font="TkTextFont")
        self.Text_kw_5_or_4.configure(foreground="black")
        self.Text_kw_5_or_4.configure(highlightbackground="#d9d9d9")
        self.Text_kw_5_or_4.configure(highlightcolor="black")
        self.Text_kw_5_or_4.configure(insertbackground="black")
        self.Text_kw_5_or_4.configure(selectbackground="#c4c4c4")
        self.Text_kw_5_or_4.configure(selectforeground="black")
        self.Text_kw_5_or_4.configure(wrap="word")

        self.Label3 = tk.Label(self.Frame_Data)
        self.Label3.place(relx=0.42, rely=0.48, height=21, width=31)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''AND''')

        self.Label3_6 = tk.Label(self.Frame_Data)
        self.Label3_6.place(relx=0.435, rely=0.72, height=21, width=26)
        self.Label3_6.configure(activebackground="#f9f9f9")
        self.Label3_6.configure(activeforeground="black")
        self.Label3_6.configure(background="#d9d9d9")
        self.Label3_6.configure(disabledforeground="#a3a3a3")
        self.Label3_6.configure(foreground="#000000")
        self.Label3_6.configure(highlightbackground="#d9d9d9")
        self.Label3_6.configure(highlightcolor="black")
        self.Label3_6.configure(text='''OR''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.551, rely=0.016, relheight=0.198, relwidth=0.43)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.017, rely=0.08, height=21, width=85)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''comment lines''')

        self.Text_commentLine_1 = tk.Text(self.Frame1)
        self.Text_commentLine_1.place(relx=0.171, rely=0.08, relheight=0.192
                , relwidth=0.81)
        self.Text_commentLine_1.configure(background="white")
        self.Text_commentLine_1.configure(font="TkTextFont")
        self.Text_commentLine_1.configure(foreground="black")
        self.Text_commentLine_1.configure(highlightbackground="#d9d9d9")
        self.Text_commentLine_1.configure(highlightcolor="black")
        self.Text_commentLine_1.configure(insertbackground="black")
        self.Text_commentLine_1.configure(selectbackground="#c4c4c4")
        self.Text_commentLine_1.configure(selectforeground="black")
        self.Text_commentLine_1.configure(wrap="word")

        self.Text_commentLine_2 = tk.Text(self.Frame1)
        self.Text_commentLine_2.place(relx=0.017, rely=0.28, relheight=0.192
                , relwidth=0.964)
        self.Text_commentLine_2.configure(background="white")
        self.Text_commentLine_2.configure(font="TkTextFont")
        self.Text_commentLine_2.configure(foreground="black")
        self.Text_commentLine_2.configure(highlightbackground="#d9d9d9")
        self.Text_commentLine_2.configure(highlightcolor="black")
        self.Text_commentLine_2.configure(insertbackground="black")
        self.Text_commentLine_2.configure(selectbackground="#c4c4c4")
        self.Text_commentLine_2.configure(selectforeground="black")
        self.Text_commentLine_2.configure(wrap="word")

        self.Text_commentLine_3 = tk.Text(self.Frame1)
        self.Text_commentLine_3.place(relx=0.017, rely=0.52, relheight=0.192
                , relwidth=0.964)
        self.Text_commentLine_3.configure(background="white")
        self.Text_commentLine_3.configure(font="TkTextFont")
        self.Text_commentLine_3.configure(foreground="black")
        self.Text_commentLine_3.configure(highlightbackground="#d9d9d9")
        self.Text_commentLine_3.configure(highlightcolor="black")
        self.Text_commentLine_3.configure(insertbackground="black")
        self.Text_commentLine_3.configure(selectbackground="#c4c4c4")
        self.Text_commentLine_3.configure(selectforeground="black")
        self.Text_commentLine_3.configure(wrap="word")

        self.Text_commentLine_4 = tk.Text(self.Frame1)
        self.Text_commentLine_4.place(relx=0.017, rely=0.76, relheight=0.192
                , relwidth=0.964)
        self.Text_commentLine_4.configure(background="white")
        self.Text_commentLine_4.configure(font="TkTextFont")
        self.Text_commentLine_4.configure(foreground="black")
        self.Text_commentLine_4.configure(highlightbackground="#d9d9d9")
        self.Text_commentLine_4.configure(highlightcolor="black")
        self.Text_commentLine_4.configure(insertbackground="black")
        self.Text_commentLine_4.configure(selectbackground="#c4c4c4")
        self.Text_commentLine_4.configure(selectforeground="black")
        self.Text_commentLine_4.configure(wrap="word")

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.0, rely=0.222, relheight=0.753, relwidth=0.982)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Btn_SearshVedios = tk.Button(self.Frame2)
        self.Btn_SearshVedios.place(relx=0.007, rely=0.0, height=34, width=123)
        self.Btn_SearshVedios.configure(activebackground="#ececec")
        self.Btn_SearshVedios.configure(activeforeground="#15c402")
        self.Btn_SearshVedios.configure(background="#00d307")
        self.Btn_SearshVedios.configure(disabledforeground="#a3a3a3")
        self.Btn_SearshVedios.configure(foreground="#000000")
        self.Btn_SearshVedios.configure(highlightbackground="#d9d9d9")
        self.Btn_SearshVedios.configure(highlightcolor="black")
        self.Btn_SearshVedios.configure(pady="0")
        self.Btn_SearshVedios.configure(text='''search Vedios''')

        self.Listbox_VideoInfo = tk.Listbox(self.Frame2)
        self.Listbox_VideoInfo.place(relx=0.007, rely=0.105, relheight=0.888
                , relwidth=0.55)
        self.Listbox_VideoInfo.configure(background="white")
        self.Listbox_VideoInfo.configure(disabledforeground="#a3a3a3")
        self.Listbox_VideoInfo.configure(font="TkFixedFont")
        self.Listbox_VideoInfo.configure(foreground="#000000")
        self.Listbox_VideoInfo.configure(highlightbackground="#d9d9d9")
        self.Listbox_VideoInfo.configure(highlightcolor="black")
        self.Listbox_VideoInfo.configure(selectbackground="#c4c4c4")
        self.Listbox_VideoInfo.configure(selectforeground="black")

        self.Listbox_CommentsList = tk.Listbox(self.Frame2)
        self.Listbox_CommentsList.place(relx=0.749, rely=0.105, relheight=0.888
                , relwidth=0.243)
        self.Listbox_CommentsList.configure(background="white")
        self.Listbox_CommentsList.configure(disabledforeground="#a3a3a3")
        self.Listbox_CommentsList.configure(font="TkFixedFont")
        self.Listbox_CommentsList.configure(foreground="#000000")

        self.Label5 = tk.Label(self.Frame2)
        self.Label5.place(relx=0.127, rely=0.021, height=21, width=117)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''max:50 Videos Num :''')

        self.Text_videosNum = tk.Text(self.Frame2)
        self.Text_videosNum.place(relx=0.21, rely=0.021, relheight=0.051
                , relwidth=0.048)
        self.Text_videosNum.configure(background="white")
        self.Text_videosNum.configure(font="TkTextFont")
        self.Text_videosNum.configure(foreground="black")
        self.Text_videosNum.configure(highlightbackground="#d9d9d9")
        self.Text_videosNum.configure(highlightcolor="black")
        self.Text_videosNum.configure(insertbackground="black")
        self.Text_videosNum.configure(selectbackground="#c4c4c4")
        self.Text_videosNum.configure(selectforeground="black")
        self.Text_videosNum.configure(wrap="word")

        self.Frame_videosCommentInfo = tk.Frame(self.Frame2)
        self.Frame_videosCommentInfo.place(relx=0.562, rely=0.105
                , relheight=0.874, relwidth=0.176)
        self.Frame_videosCommentInfo.configure(relief='groove')
        self.Frame_videosCommentInfo.configure(borderwidth="2")
        self.Frame_videosCommentInfo.configure(relief="groove")
        self.Frame_videosCommentInfo.configure(background="#d9d9d9")

        self.Label_VideosInfo1 = tk.Label(self.Frame_videosCommentInfo)
        self.Label_VideosInfo1.place(relx=0.043, rely=0.048, height=21
                , width=212)
        self.Label_VideosInfo1.configure(activebackground="#f9f9f9")
        self.Label_VideosInfo1.configure(activeforeground="black")
        self.Label_VideosInfo1.configure(anchor='w')
        self.Label_VideosInfo1.configure(background="#d9d9d9")
        self.Label_VideosInfo1.configure(disabledforeground="#a3a3a3")
        self.Label_VideosInfo1.configure(foreground="#000000")
        self.Label_VideosInfo1.configure(highlightbackground="#d9d9d9")
        self.Label_VideosInfo1.configure(highlightcolor="black")

        self.Label_VideosInfo2 = tk.Label(self.Frame_videosCommentInfo)
        self.Label_VideosInfo2.place(relx=0.043, rely=0.12, height=21, width=212)

        self.Label_VideosInfo2.configure(activebackground="#f9f9f9")
        self.Label_VideosInfo2.configure(activeforeground="black")
        self.Label_VideosInfo2.configure(anchor='w')
        self.Label_VideosInfo2.configure(background="#d9d9d9")
        self.Label_VideosInfo2.configure(disabledforeground="#a3a3a3")
        self.Label_VideosInfo2.configure(foreground="#000000")
        self.Label_VideosInfo2.configure(highlightbackground="#d9d9d9")
        self.Label_VideosInfo2.configure(highlightcolor="black")

        self.Label_VideosInfo3 = tk.Label(self.Frame_videosCommentInfo)
        self.Label_VideosInfo3.place(relx=0.043, rely=0.193, height=21
                , width=212)
        self.Label_VideosInfo3.configure(activebackground="#f9f9f9")
        self.Label_VideosInfo3.configure(activeforeground="black")
        self.Label_VideosInfo3.configure(anchor='w')
        self.Label_VideosInfo3.configure(background="#d9d9d9")
        self.Label_VideosInfo3.configure(disabledforeground="#a3a3a3")
        self.Label_VideosInfo3.configure(foreground="#000000")
        self.Label_VideosInfo3.configure(highlightbackground="#d9d9d9")
        self.Label_VideosInfo3.configure(highlightcolor="black")

        self.Label_VideosInfo4 = tk.Label(self.Frame_videosCommentInfo)
        self.Label_VideosInfo4.place(relx=0.043, rely=0.265, height=21
                , width=212)
        self.Label_VideosInfo4.configure(activebackground="#f9f9f9")
        self.Label_VideosInfo4.configure(activeforeground="black")
        self.Label_VideosInfo4.configure(anchor='w')
        self.Label_VideosInfo4.configure(background="#d9d9d9")
        self.Label_VideosInfo4.configure(disabledforeground="#a3a3a3")
        self.Label_VideosInfo4.configure(foreground="#000000")
        self.Label_VideosInfo4.configure(highlightbackground="#d9d9d9")
        self.Label_VideosInfo4.configure(highlightcolor="black")

        self.Label_VideosInfo5 = tk.Label(self.Frame_videosCommentInfo)
        self.Label_VideosInfo5.place(relx=0.043, rely=0.337, height=21
                , width=212)
        self.Label_VideosInfo5.configure(activebackground="#f9f9f9")
        self.Label_VideosInfo5.configure(activeforeground="black")
        self.Label_VideosInfo5.configure(anchor='w')
        self.Label_VideosInfo5.configure(background="#d9d9d9")
        self.Label_VideosInfo5.configure(disabledforeground="#a3a3a3")
        self.Label_VideosInfo5.configure(foreground="#000000")
        self.Label_VideosInfo5.configure(highlightbackground="#d9d9d9")
        self.Label_VideosInfo5.configure(highlightcolor="black")

        self.Label_VideosInfo6 = tk.Label(self.Frame_videosCommentInfo)
        self.Label_VideosInfo6.place(relx=0.043, rely=0.41, height=21, width=212)

        self.Label_VideosInfo6.configure(activebackground="#f9f9f9")
        self.Label_VideosInfo6.configure(activeforeground="black")
        self.Label_VideosInfo6.configure(anchor='w')
        self.Label_VideosInfo6.configure(background="#d9d9d9")
        self.Label_VideosInfo6.configure(disabledforeground="#a3a3a3")
        self.Label_VideosInfo6.configure(foreground="#000000")
        self.Label_VideosInfo6.configure(highlightbackground="#d9d9d9")
        self.Label_VideosInfo6.configure(highlightcolor="black")

        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.007, rely=0.0, relheight=0.055, relwidth=0.283)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")

        self.Radiobutton1 = tk.Radiobutton(self.Frame3)
        self.Radiobutton1.place(relx=0.026, rely=0.143, relheight=0.714
                , relwidth=0.151)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''1''')
        self.Radiobutton1.configure(variable=main_support.selectedButton)

        self.Radiobutton1_8 = tk.Radiobutton(self.Frame3)
        self.Radiobutton1_8.place(relx=0.156, rely=0.143, relheight=0.714
                , relwidth=0.151)
        self.Radiobutton1_8.configure(activebackground="#ececec")
        self.Radiobutton1_8.configure(activeforeground="#000000")
        self.Radiobutton1_8.configure(background="#d9d9d9")
        self.Radiobutton1_8.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_8.configure(foreground="#000000")
        self.Radiobutton1_8.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_8.configure(highlightcolor="black")
        self.Radiobutton1_8.configure(justify='left')
        self.Radiobutton1_8.configure(text='''2''')
        self.Radiobutton1_8.configure(variable=main_support.selectedButton)

        self.Radiobutton1_9 = tk.Radiobutton(self.Frame3)
        self.Radiobutton1_9.place(relx=0.312, rely=0.143, relheight=0.714
                , relwidth=0.151)
        self.Radiobutton1_9.configure(activebackground="#ececec")
        self.Radiobutton1_9.configure(activeforeground="#000000")
        self.Radiobutton1_9.configure(background="#d9d9d9")
        self.Radiobutton1_9.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_9.configure(foreground="#000000")
        self.Radiobutton1_9.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_9.configure(highlightcolor="black")
        self.Radiobutton1_9.configure(justify='left')
        self.Radiobutton1_9.configure(text='''3''')
        self.Radiobutton1_9.configure(variable=main_support.selectedButton)

        self.Radiobutton1_10 = tk.Radiobutton(self.Frame3)
        self.Radiobutton1_10.place(relx=0.468, rely=0.143, relheight=0.714
                , relwidth=0.151)
        self.Radiobutton1_10.configure(activebackground="#ececec")
        self.Radiobutton1_10.configure(activeforeground="#000000")
        self.Radiobutton1_10.configure(background="#d9d9d9")
        self.Radiobutton1_10.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_10.configure(foreground="#000000")
        self.Radiobutton1_10.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_10.configure(highlightcolor="black")
        self.Radiobutton1_10.configure(justify='left')
        self.Radiobutton1_10.configure(text='''4''')
        self.Radiobutton1_10.configure(variable=main_support.selectedButton)

        self.Radiobutton1_11 = tk.Radiobutton(self.Frame3)
        self.Radiobutton1_11.place(relx=0.623, rely=0.143, relheight=0.714
                , relwidth=0.151)
        self.Radiobutton1_11.configure(activebackground="#ececec")
        self.Radiobutton1_11.configure(activeforeground="#000000")
        self.Radiobutton1_11.configure(background="#d9d9d9")
        self.Radiobutton1_11.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_11.configure(foreground="#000000")
        self.Radiobutton1_11.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_11.configure(highlightcolor="black")
        self.Radiobutton1_11.configure(justify='left')
        self.Radiobutton1_11.configure(text='''5''')
        self.Radiobutton1_11.configure(variable=main_support.selectedButton)

        self.Radiobutton1_12 = tk.Radiobutton(self.Frame3)
        self.Radiobutton1_12.place(relx=0.831, rely=0.143, relheight=0.714
                , relwidth=0.151)
        self.Radiobutton1_12.configure(activebackground="#ececec")
        self.Radiobutton1_12.configure(activeforeground="#000000")
        self.Radiobutton1_12.configure(background="#d9d9d9")
        self.Radiobutton1_12.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_12.configure(foreground="#000000")
        self.Radiobutton1_12.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_12.configure(highlightcolor="black")
        self.Radiobutton1_12.configure(justify='left')
        self.Radiobutton1_12.configure(text='''6''')
        self.Radiobutton1_12.configure(variable=main_support.selectedButton)

if __name__ == '__main__':
    vp_start_gui()





