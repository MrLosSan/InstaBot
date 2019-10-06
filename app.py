print ("Welcome to InstaBot made by Iconz")#line:1
client_name =input ("Email: ")#line:3
client_pass =input ("Password: ")#line:4
from selenium import webdriver #line:6
from selenium .webdriver .common .keys import Keys #line:7
import time #line:8
class TwitterBot :#line:11
    def __init__ (OOO0O000OO000O00O ,OO0O0OOO00O000O00 ,O0OOOOO0O00OO0O00 ):#line:12
        OOO0O000OO000O00O .username =OO0O0OOO00O000O00 #line:13
        OOO0O000OO000O00O .password =O0OOOOO0O00OO0O00 #line:14
        OOO0O000OO000O00O .bot =webdriver .Firefox ()#line:15
    def login (O0O000O0O0OO0OOOO ):#line:17
        O00O00OO0OOO00O00 =O0O000O0O0OO0OOOO .bot #line:18
        O00O00OO0OOO00O00 .get ('https://www.instagram.com/accounts/login/')#line:19
        time .sleep (4 )#line:20
        OO0OOO0OOOOOO00OO =O00O00OO0OOO00O00 .find_element_by_name ('username')#line:21
        O00OO000O00O0OOO0 =O00O00OO0OOO00O00 .find_element_by_name ('password')#line:22
        OO0OOO0OOOOOO00OO .clear ()#line:23
        O00OO000O00O0OOO0 .clear ()#line:24
        OO0OOO0OOOOOO00OO .send_keys (O0O000O0O0OO0OOOO .username )#line:25
        O00OO000O00O0OOO0 .send_keys (O0O000O0O0OO0OOOO .password )#line:26
        O00OO000O00O0OOO0 .send_keys (Keys .RETURN )#line:27
        time .sleep (4 )#line:28
        O00O00OO0OOO00O00 .find_element_by_xpath ('/html/body/div[3]/div/div/div[3]/button[2]').click ()#line:29
    def follow (O0OO000O0OO0000OO ):#line:31
        OOOOO00OOOOO0000O =O0OO000O0OO0000OO .bot #line:32
        OO00O0OO0O0O0O0O0 =0 #line:33
        OO0O0OO000000O0OO =0 #line:34
        OOO00O00O000000OO =0 #line:35
        for OO00OO0O0O00O0OOO in range (1 ,1000000 ):#line:36
            OOOOO00OOOOO0000O .get ('https://www.instagram.com/explore/people/suggested/')#line:37
            time .sleep (5 )#line:38
            OOOOO00OOOOO0000O .find_element_by_tag_name ('button').click ()#line:39
            OO00O0OO0O0O0O0O0 =OO00O0OO0O0O0O0O0 +1 #line:40
            print ("Followed: "+str (OO00O0OO0O0O0O0O0 ))#line:41
            OOOOO00OOOOO0000O .get ('https://www.instagram.com/')#line:42
            time .sleep (4 )#line:43
            OOOOO00OOOOO0000O .find_element_by_xpath ('/html/body/span/section/main/section/div[1]/div[2]/div/article[1]/div[2]/section[1]/span[1]/button').click ()#line:44
            OO0O0OO000000O0OO =OO0O0OO000000O0OO +1 #line:45
            print ("Liked: "+str (OO0O0OO000000O0OO ))#line:46
ed =TwitterBot (client_name ,client_pass )#line:49
ed .login ()#line:50
ed .follow ()#line:51
