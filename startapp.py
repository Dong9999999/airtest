# -*- encoding=utf8 -*-
__author__ = "user"

from airtest.core.api import *


auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def restart(usrname,password):   
    start_app("com.bosma.smarthome")
    sleep(10)
    if poco(text="LOG IN").exists():
        print("未登录帐号，先登录：")
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").offspring("android.widget.ScrollView").offspring("com.bosma.smarthome:id/ciUserCenterLoginAccount").offspring("android.widget.LinearLayout").offspring("com.bosma.smarthome:id/etCommonItem").set_text(usrname)



        poco(text="Password").set_text(password)

        poco("com.bosma.smarthome:id/clLoginContainer").click()
        poco(text="LOG IN").click()
        sleep(10)

    elif poco(text="Common").exists():
        
        print("已登录，继续测试")
        

# print("在首页，点击轮播图")
# device_list=[]
# device_status=[]
# a=1
# while a<10:

#     poco("com.bosma.smarthome:id/bannerImage").click()
#     sleep(10)
#     print("进入Liveview：")
#     ele=poco("com.bosma.smarthome:id/tvToolbarTitle")
#     device_name=ele.attr("text")
#     #实时预览，设备不在线
#     if poco(text="Device offline").exists():


#         print(f'{ele.attr("text")}设备离线')
#         device_status.append('设备离线')


#         poco("Navigate up").click()
#         print("返回首页")
#     #实时预览设备在线    
#     elif poco("com.bosma.smarthome:id/tvCommonVideoDeviceHealthContainerBitRate").exists():
#         print("正在实时预览，等待60s")
#         sleep(60)
#         print(f'预览设备{ele.attr("text")} 预览了60s')
#         device_status.append('设备在线预览了60s')
#         poco("Navigate up").click()
#         print("返回首页")
#     #实时预览，加载失败
#     else:
#         print(f'等待了10s，{ele.attr("text")}设备视频加载不成，但又没提示离线')
#         device_status.append('设备视频加载不成，但又没提示离线')
#         poco("Navigate up").click()
#         print("返回首页")
#     sleep(5)    
#     a=a+1
#     device_list.append(ele.attr("text"))
# i=0  
# print ("从轮播图进入Liveview，共检查了以下设备：")
# for i in range(len(device_list)):

#     print(device_list[i],device_status[i])


#restart(usrname="qwer1@chacuo.net",password="1234qwer")        
        


    



    


    
 
    
    



