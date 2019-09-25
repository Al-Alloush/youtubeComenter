#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Sep 19, 2019 03:05:58 PM CEST  platform: Windows NT

import sys

from rsa import prime

try:
    import Tkinter as tk
    from Tkinter import *
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import main_support


from googleapiclient.discovery import build
from datetime import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
import webbrowser
import time




# ----------------------------------

oAuthDay = 3

END_MONTH = 8  # if 7 that mean the month 8 then stop

API_KEY =''
CLIENT_SECRET_FILE= ''

if oAuthDay == 1:
    #
    #API_KEY ='AIzaSyBjW7nrfW6YTAfq9nSeY8Z9torqvfRveWc'
    API_KEY = 'AIzaSyBSV0EknK3T8Ytd8FUPTC_s_poPJI-XmhY'
    CLIENT_SECRET_FILE = 'client_secret_fashion1.json'
elif oAuthDay == 2:
    # -------------------------------------------Blocked by Google
    API_KEY = ''
    CLIENT_SECRET_FILE = ''
elif oAuthDay == 3:
    #
    API_KEY = 'AIzaSyDtBAjjkDwXCvxdy5_dCHmJlbdIGWfXiNk'
    CLIENT_SECRET_FILE = 'client_secret_fashion3.json'
elif oAuthDay == 4:
    #
    API_KEY = 'AIzaSyAEHNGwRhAf4LEHd2soUFU6sBYjGn3HMu8'
    CLIENT_SECRET_FILE = 'client_secret_fashion4.json'
elif oAuthDay == 5:
    #
    API_KEY = 'AIzaSyDF31al5C5rz3Ilm8m7MhIyvupcYigJU2U'
    CLIENT_SECRET_FILE = 'client_secret_fashion5.json'
elif oAuthDay == 6:
    #
    API_KEY = 'AIzaSyCpUhp397gwbixVxVXmy2gJbns1FqC5BTg'
    CLIENT_SECRET_FILE = 'client_secret_fashion6.json'
elif oAuthDay == 7:
    # appdev Account
    API_KEY = 'AIzaSyD0UzhyQ2H6XEQo1aHdi_T1YDVmbcuNdt4'
    CLIENT_SECRET_FILE = 'client_secret_appdev.json'
elif oAuthDay == 8:
    # alloush.dev1 Account
    API_KEY = 'AIzaSyCvpqGWudLD-GlGUNlZkC5u2CwncyPICIU'
    CLIENT_SECRET_FILE = ''

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]


# ---------------------------------

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    main_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None




class Toplevel1:

    successAuth = False
    youtube = ''

    def createOAuth(self):
        # start to Authentication with google Account
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)

        # credentials = flow.run_console()
        credentials = flow.run_local_server()

        self.youtube = build('youtube', 'v3', credentials=credentials)
        if self.youtube:
            print('Successful Authentication connection')
            self.successAuth = True
            self.Label_OAuth.configure(text='''success Auth''')
        else:
            self.Label_OAuth.configure(text='''Error Not Auth''')
            print('Error Not Authentication')

    def startComments(self):

        self.successAuth = True

        if self.successAuth:

            # get the key words
            key_1 = self.Text_kw_1.get("1.0", 'end-1c')

            key_2and3 = self.Text_kw_2_and_3.get("1.0", 'end-1c')
            key_3and2 = self.Text_kw_3_and_2.get("1.0", 'end-1c')

            key_4or5 = self.Text_kw_4_or_5.get("1.0", 'end-1c')
            key_5or4 = self.Text_kw_5_or_4.get("1.0", 'end-1c')


            # get the comments
            comnt1 = self.Text_commentLine_1.get("1.0", 'end-1c')
            comnt2 = self.Text_commentLine_2.get("1.0", 'end-1c')
            comnt3 = self.Text_commentLine_3.get("1.0", 'end-1c')
            comnt4 = self.Text_commentLine_4.get("1.0", 'end-1c')

            # get the videos numbers max 50
            videosNum = int(self.Text_videosNum.get("1.0", 'end-1c'))



            date_nowr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            date_year = int(datetime.now().strftime('%Y'))
            date_month = int(datetime.now().strftime('%m'))
            date_day = int(datetime.now().strftime('%d'))
            date_day -=1  # to start from day before Now

            youtubeSearch = build('youtube', 'v3', developerKey=API_KEY)

            print('the time now is : '+ str(date_year))

            days_counter = 0
            month_counter = 0
            comments_id = 0
            # Decrease the years from Now Eg. 2019
            while date_year > 2018:
                while date_month > END_MONTH:
                    while date_day > 0:
                        print(); print()
                        print('---------------------  '+str(date_year) + '/' + str(date_month) + '/' + str(date_day))  # day before
                        print('comments Num: ' + str(comments_id) + ' -Days: ' + str(days_counter) + ' -Months: ' + str(month_counter))
                        print(); print()

                        # crate Http Request for Search
                        youtubeSerch = build('youtube', 'v3', developerKey=API_KEY)

                        # set the time to start and finish
                        # '%Y-%m-%dT%H:%M:%SZ' form out Eg. 2019-01-01T00:00:00Z
                        start_time = datetime(year=date_year, month=date_month, day=date_day, hour=0, minute=0, second=0).strftime( '%Y-%m-%dT%H:%M:%SZ')
                        end_time = datetime(year=date_year, month=date_month, day=date_day, hour=23, minute=59, second=59).strftime( '%Y-%m-%dT%H:%M:%SZ')

                        # set the 5 Keywords in Http request
                        if key_1 == '' and key_2and3 != '' and key_3and2 != '':
                            req = youtubeSerch.search().list(q=key_2and3 and key_3and2, part='snippet', type="video", maxResults=videosNum, publishedAfter=start_time, publishedBefore=end_time)
                        elif key_4or5 != '' and key_5or4 != '':
                            req = youtubeSerch.search().list(q=key_4or5 or key_5or4, part='snippet', type="video", maxResults=videosNum, publishedAfter=start_time, publishedBefore=end_time)
                        else:
                            req = youtubeSerch.search().list(q=key_1, part='snippet', type="video", maxResults=videosNum, publishedAfter=start_time, publishedBefore=end_time)
                        # execute the Http Request
                        response = req.execute()

                        # get the Item number found in date_day value
                        itemsNum = len(response['items'])
                        print('Found Item : ' + str(itemsNum))


                        # start Like and Comments
                        for item in response['items']:
                            try:
                                # get the data from item
                                channelId = item['snippet']['channelId']
                                videoId = item['id']['videoId']
                                videoTitle = item['snippet']['title']


                                # like this video
                                self.youtube.videos().rate(rating='like', id=videoId).execute()

                                # Comments Part
                                if comnt1 != '' and comnt2 == '':
                                    insert_result = self.youtube.commentThreads().insert(
                                        part="snippet",
                                        body=dict(
                                            snippet=dict(
                                                channelId=channelId,
                                                videoId=videoId,
                                                topLevelComment=dict(
                                                    snippet=dict(
                                                        textOriginal=comnt1)
                                                )
                                            )
                                        )
                                    ).execute()
                                    comment = insert_result["snippet"]["topLevelComment"]
                                    author = comment["snippet"]["authorDisplayName"]
                                    text = comment["snippet"]["textDisplay"]
                                    print("Inserted comment for %s: %s" % (author, text))
                                elif comnt1 != '' and comnt2 != '' and comnt3 == '':
                                    insert_result = self.youtube.commentThreads().insert(
                                        part="snippet",
                                        body=dict(
                                            snippet=dict(
                                                channelId=channelId,
                                                videoId=videoId,
                                                topLevelComment=dict(
                                                    snippet=dict(
                                                        textOriginal=comnt1 + '\n' + comnt2)
                                                )
                                            )
                                        )
                                    ).execute()
                                    comment = insert_result["snippet"]["topLevelComment"]
                                    author = comment["snippet"]["authorDisplayName"]
                                    text = comment["snippet"]["textDisplay"]
                                    print("Inserted comment for %s: %s" % (author, text))
                                elif comnt1 != '' and comnt2 != '' and comnt3 != '' and comnt4 == '':
                                    insert_result = self.youtube.commentThreads().insert(
                                        part="snippet",
                                        body=dict(
                                            snippet=dict(
                                                channelId=channelId,
                                                videoId=videoId,
                                                topLevelComment=dict(
                                                    snippet=dict(
                                                        textOriginal=comnt1 + '\n' + comnt2 + '\n' + comnt3)
                                                )
                                            )
                                        )
                                    ).execute()
                                    comment = insert_result["snippet"]["topLevelComment"]
                                    author = comment["snippet"]["authorDisplayName"]
                                    text = comment["snippet"]["textDisplay"]
                                    print("Inserted comment for %s: %s" % (author, text))
                                elif comnt1 != '' and comnt2 != '' and comnt3 != '' and comnt4 != '':
                                    insert_result = self.youtube.commentThreads().insert(
                                        part="snippet",
                                        body=dict(
                                            snippet=dict(
                                                channelId=channelId,
                                                videoId=videoId,
                                                topLevelComment=dict(
                                                    snippet=dict(
                                                        textOriginal=comnt1 + '\n' + comnt2 + '\n' + comnt3 + '\n' + comnt4)
                                                )
                                            )
                                        )
                                    ).execute()
                                    comment = insert_result["snippet"]["topLevelComment"]
                                    author = comment["snippet"]["authorDisplayName"]
                                    text = comment["snippet"]["textDisplay"]
                                    print("Inserted comment for %s: %s" % (author, text))
                                # End Comments Part

                                print('https://www.youtube.com/watch?v=' + videoId)

                                # sleep somtime
                                time.sleep(5.5)  # pause 5.5 seconds

                                # set links in Comments List
                                self.Listbox_CommentsList.insert(comments_id, 'https://www.youtube.com/watch?v=' + videoId)

                                # set Titels and someinfo in  in Listbox_Video Info List
                                self.Listbox_VideoInfo.insert(comments_id, 'Title: ' + videoTitle)

                                comments_id += 1
                            except Exception as e:
                                print('exception _____________________________')
                                print(e)
                                print('exception _____________________________')


                        # to stop the comment at the fierst loop to Teset it
                        #date_day = 0
                        #date_month = 0
                        #date_year=0


                        # to Now the Numbers of days has Comment in
                        days_counter += 1
                        # this Days Counter
                        date_day -= 1

                        # --------------------------------------------------- END Days Loop
                    # to Now the Numbers of months has Comment in
                    month_counter += 1
                    # Decrease Month counter befor set the next month days
                    date_month -= 1  # this Month Counter
                    # after End Days Loop set the Next Month days. Eg. month 1 has 31 days, month 2 has 28 days , month 2 has 30 days, ....
                    date_day = 30  # standard days number for month
                    if date_month == 2:
                        date_day = 28  # if month is 2 his days are 28

                    if date_month == 1 or date_month < 1 \
                            or date_month == 3 or date_month == 5 or date_month == 7 \
                            or date_month == 8 or date_month == 10 or date_month == 12:
                        date_day = 31  # if month is one of above numbers his days are 31
                    #  ------------------------------------------------------------------------------ END Month Loop
                # after END month loop set the months number for every year
                date_month = 12
                # this Year Counter
                date_year -= 1
                # -------------------------------------------------------------------------------------------------- END Year Loop

            print('days Numbers are: '+ str(days_counter) + ' and months Numbers are: ' + str(month_counter))

            s_comments_id = 'comments Number: ' + str(comments_id)
            self.Label_VideosInfo1.configure(text=s_comments_id)

            s_days_counter = 'Days: ' + str(days_counter)
            self.Label_VideosInfo2.configure(text=s_days_counter)

            s_month_counter = 'Months: ' + str(month_counter)
            self.Label_VideosInfo3.configure(text=s_month_counter)


        else:
            self.Label_OAuth.configure(text='''Need to Auth''')
        # ========================================================== END startComments Function

    def openLink(self):
        index = self.Listbox_CommentsList.curselection()[0]
        link =  self.Listbox_CommentsList.get(index)
        webbrowser.open_new_tab(link)
        print(link)

    def __init__(self, top=None):
        ''''This class configures and populates the toplevel window.
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
        self.Frame_OAuth.place(relx=0.007, rely=0.016, relheight=0.151
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
        self.Btn_SearshVedios.configure(text='''Start Comments''')

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



        # -------------------------------------------------

        self.Btn_SearshVedios.configure(command = self.startComments)

        self.Btn_OAuth.configure(command = self.createOAuth)

        self.Listbox_CommentsList.bind("<<ListboxSelect>>", lambda x: self.openLink())


        self.Text_videosNum.insert('0.0', '3')


if __name__ == '__main__':
    vp_start_gui()





