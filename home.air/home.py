# -*- encoding=utf8 -*-
__author__ = "user"

from airtest.core.api import *
from my_api.startapp import restart
from airtest.cli.parser import cli_setup
 
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from airtest.core.android.adb import *
from airtest.core.android.android import *
import time
dev = device()

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#restart(usrname="qwer5@chacuo.net",password="1234qwer")
def Home_Live():
#首页轮播图进入实时
    print("在首页，点击轮播图")
    device_list=[]
    device_status=[]
    a=1
    while a<3:

        poco("com.bosma.smarthome:id/bannerImage").click()
        sleep(10)
        print("进入Liveview：")
        ele=poco("com.bosma.smarthome:id/tvToolbarTitle")
        device_name=ele.attr("text")
        #实时预览，设备不在线
        if poco(text="Device offline").exists():


            print(f'{ele.attr("text")}设备离线')
            device_status.append('设备离线')


            poco("Navigate up").click()
            print("返回首页")
        #实时预览设备在线    
        elif poco("com.bosma.smarthome:id/tvCommonVideoDeviceHealthContainerBitRate").exists():
            print("正在实时预览，等待60s")
            sleep(60)
            print(f'预览设备{ele.attr("text")} 预览了60s')
            device_status.append('设备在线预览了60s')
            poco("Navigate up").click()
            print("返回首页")
        #实时预览，加载失败
        else:
            print(f'等待了10s，{ele.attr("text")}设备视频加载不成，但又没提示离线')
            device_status.append('设备视频加载不成，但又没提示离线')
            poco("Navigate up").click()
            print("返回首页")
        sleep(5)    
        a=a+1
        device_list.append(ele.attr("text"))
    i=0  
    print ("从轮播图进入Liveview，共检查了以下设备：")
    for i in range(len(device_list)):

        print(device_list[i],device_status[i])

#首页轮播图进入事件列表
def Home_Event():
    b=1
    print("测试首页轮播图进入事件列表：")
    while b<10:
        sleep(5)
        poco("com.bosma.smarthome:id/ivDeviceListIcon").click()
        sleep(5)
        if poco("com.bosma.smarthome:id/tvCommonEventCenterEventListNewNoDataTips").exists():
            print("当天没有事件")
            sleep(2)
            poco("Navigate up").click()
            print("返回首页")
        else:
            bb=poco("com.bosma.smarthome:id/rcvCommonEventCenterEventListNewEventContainer").child("com.bosma.smarthome:id/llItemCommonEventListContainer")[0].offspring("com.bosma.smarthome:id/tvCommonCenterListItemDeviceNick")


            aa=poco("com.bosma.smarthome:id/rcvCommonEventCenterEventListNewEventContainer").child("com.bosma.smarthome:id/llItemCommonEventListContainer")
            event_list=list(aa)


            for j in range (len(event_list)):

                event_list[j].offspring("com.bosma.smarthome:id/ivCommonEventListItemEventPlay").click() 
                sleep(30)

            print(f'点击播放了{bb.attr("text")}设备{len(event_list)}个事件，返回首页')
            poco("Navigate up").click()
        b=b+1


#首页轮播图进入设置
def Home_Setting():
    
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    c=1
    print("测试首页轮播图进入设置页：")
    while c<4:
        sleep(5)
        poco("com.bosma.smarthome:id/ivSettingIcon").click()
        sleep(5)
        if poco("com.bosma.smarthome:id/tv_offline_tips").exists():
            cc=poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.bosma.smarthome:id/navHostDeviceSettingContainer").offspring("com.bosma.smarthome:id/contentPanel").offspring("com.bosma.smarthome:id/deviceSettingRecyclerView").child("android.widget.LinearLayout")[0].offspring("com.bosma.smarthome:id/rlCustomSettingItem").offspring("com.bosma.smarthome:id/tvRight")
            print(f'{cc.attr("text")}设备离线，设置页提示离线')
            poco("Navigate up").click()
        elif poco(text="Event & Notification").exists():

            poco = AndroidUiautomationPoco(device=dev, use_airtest_input=True, screenshot_each_action=False)
            # 获取设备的高度和宽度
            width, height = poco.get_screen_size()
            # 校准滑动的起点和终点
            start_pt = (width * 0.5, height * 0.8)
            end_pt = (width * 0.5, height * 0.2)
            for i in range(6):
                swipe(start_pt, end_pt)
                time.sleep(1)
            dd=poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.bosma.smarthome:id/navHostDeviceSettingContainer").offspring("com.bosma.smarthome:id/contentPanel").offspring("com.bosma.smarthome:id/deviceSettingRecyclerView").child("android.widget.LinearLayout")[0].offspring("com.bosma.smarthome:id/rlCustomSettingItem").offspring("com.bosma.smarthome:id/tvRight")
            print(f'{dd.attr("text")}设备在线，设置页显示正常')
            poco("Navigate up").click()

        else:
            print("设置页加载失败")
            poco("Navigate up").click()
        c=c+1
#首页切换场景
def Home_Security_Mode():
   
    a=0
    while a<3:
        sleep(2)
        poco("com.bosma.smarthome:id/layoutHomeCommonScene").click()


        #aa=poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.bosma.smarthome:id/smHomeSideMenu").offspring("com.bosma.smarthome:id/fl_fragment_container").offspring("android.widget.ScrollView").offspring("com.bosma.smarthome:id/rvHomeCommonSubSystem").child("com.bosma.smarthome:id/flSceneItemBg")[1].offspring("com.bosma.smarthome:id/tvSceneName")
        bb=poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.bosma.smarthome:id/smHomeSideMenu").offspring("com.bosma.smarthome:id/fl_fragment_container").offspring("android.widget.ScrollView").offspring("com.bosma.smarthome:id/rvHomeCommonSubSystem").child("com.bosma.smarthome:id/flSceneItemBg")
        scene_list=list(bb)
        #print(scene_list)
        #for i in range(len(scene_list)):
        scene_list[a].click()
        poco("com.bosma.smarthome:id/tvSceneExecute").click()
        d=1
        while d==1:
            sleep(5)
            if poco("com.bosma.smarthome:id/tvExecuteOk").exists():
                break
        dd=poco("com.bosma.smarthome:id/tvExecuteSceneName")
        print(f'切换到{dd.attr("text")}场景')
        poco("com.bosma.smarthome:id/tvExecuteOk").click()
        a=a+1

#首页进入云服务测试
def Bosma_Assist():
    poco(text="Bosma Assist").click()
    sleep(5)
    tab=poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android.widget.LinearLayout").child("android.webkit.WebView").child("android.webkit.WebView").offspring("app").child("android.view.View").child("android.view.View")[0].child("android.view.View")
    tab_list=list(tab)

    #poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android.widget.LinearLayout").child("android.webkit.WebView").child("android.webkit.WebView").offspring("app").child("android.view.View").child("android.view.View")[0].child("android.view.View")[0].child("android.widget.TextView")[0]


    for i in range(len(tab_list)):
        a=tab_list[i].child("android.widget.TextView")[1]
        print(f'进入{a.attr("text")}页面')
        tab_list[i].click()
        sleep(5) 
        print(f'退出{a.attr("text")}页面')
        poco("Navigate up").click()
        sleep(3)
    print("退出云服务页面，返回首页")
    poco("Navigate up").click()


#首页设备列表

def Home_Devices():
    
    if poco("com.bosma.smarthome:id/tvHomeDeviceList").exists():
        #home_devices=poco("com.bosma.smarthome:id/rvHomeDevicesList")
        home_devices=poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.bosma.smarthome:id/smHomeSideMenu").offspring("com.bosma.smarthome:id/fl_fragment_container").offspring("android.widget.ScrollView").offspring("com.bosma.smarthome:id/rvHomeDevicesList").child("android.widget.FrameLayout")
      
        home_devices_list=list(home_devices)


        print(f'首页设备模块有{len(home_devices_list)}个设备')
        for i in range (len(home_devices_list)):
            device_name=home_devices_list[i].offspring("com.bosma.smarthome:id/tvCardViewText")
            device_status=home_devices_list[i].offspring("com.bosma.smarthome:id/tvSubCardViewText")
            device_name.click()
            sleep(5)
            poco("Navigate up").click()
            sleep(3)
            print(f'{device_name.attr("text")}设备：{device_status.attr("text")}')

    else:
        print("首页设备栏没有设备")





