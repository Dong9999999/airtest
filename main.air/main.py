
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from airtest.core.android.adb import *
from airtest.core.android.android import *
ST.PROJECT_ROOT="D:\AirtestIDE\my_api"

using(r"startapp.air")
using(r"home.air")
from startapp import restart
from home import Home_Live,Home_Event,Home_Setting
import time
#class_name = '0ade5fc00bffda78'
#connect_device(f"Android:///{class_name}?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH")
#set_current(class_name)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
dev = device()
 
#restart(usrname="qwer5@chacuo.net",password="1234qwer")
#Home_Live()
#Home_Setting()
Home_Event()