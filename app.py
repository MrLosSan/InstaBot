from selenium import webdriver #line:1
from selenium .webdriver .common .keys import Keys #line:2
import time #line:3
print ("Welcome to AutoFollower Bot for Instagram. Made by Iconz")#line:5
username =input ("Email: ")#line:6
password =input ("Password: ")#line:7
class TwitterBot :#line:8
    def __init__ (OOOO0O00OOOOOOOO0 ,O0OOOO0O0000OO0OO ,O00OOOOO00000O00O ):#line:9
        OOOO0O00OOOOOOOO0 .username =O0OOOO0O0000OO0OO #line:10
        OOOO0O00OOOOOOOO0 .password =O00OOOOO00000O00O #line:11
        OOOO0O00OOOOOOOO0 .bot =webdriver .Firefox ()#line:12
    def login (O0OOOOO000OO0O0OO ):#line:14
        OO0O000O00000OOOO =O0OOOOO000OO0O0OO .bot #line:15
        OO0O000O00000OOOO .get ('https://www.instagram.com/accounts/login/')#line:16
        time .sleep (4 )#line:17
        OO00O000O0OOO0OO0 =OO0O000O00000OOOO .find_element_by_name ('username')#line:18
        OO000O00000000O00 =OO0O000O00000OOOO .find_element_by_name ('password')#line:19
        OO00O000O0OOO0OO0 .clear ()#line:20
        OO000O00000000O00 .clear ()#line:21
        OO00O000O0OOO0OO0 .send_keys (O0OOOOO000OO0O0OO .username )#line:22
        OO000O00000000O00 .send_keys (O0OOOOO000OO0O0OO .password )#line:23
        OO000O00000000O00 .send_keys (Keys .RETURN )#line:24
        time .sleep (4 )#line:25
    def follow (OO0O0OOO0OOO0000O ):#line:27
        O0O0000OOOOO00O0O =OO0O0OOO0OOO0000O .bot #line:28
        OO00000O0OOOO00OO =0 #line:29
        for OOOO00000000O00O0 in range (1 ,1000000 ):#line:30
            O0O0000OOOOO00O0O .get ('https://www.instagram.com/explore/people/suggested/')#line:31
            time .sleep (5 )#line:32
            O0O0000OOOOO00O0O .find_element_by_tag_name ('button').click ()#line:33
            OO00000O0OOOO00OO =OO00000O0OOOO00OO +1 #line:34
            print ("Followed: "+str (OO00000O0OOOO00OO ))#line:35
ed =TwitterBot (username ,password )#line:42
ed .login ()#line:43
ed .follow ()