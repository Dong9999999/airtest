# -*- encoding=utf8 -*-
__author__ = "user"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
def Events_list_Play():
    
   
    poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.bosma.smarthome:id/smHomeSideMenu").offspring("com.bosma.smarthome:id/fl_fragment_container").child("android.widget.LinearLayout").offspring("android.widget.LinearLayout").child("android.widget.RelativeLayout")[1].offspring("com.bosma.smarthome:id/iv_tab_icon").click()
    i=0
    while i<3:



        event=poco("com.bosma.smarthome:id/rcvCommonEventCenterEventListNewEventContainer").offspring("com.bosma.smarthome:id/llItemCommonEventListContainer")
        event_list=list(event)
        #print(event_list)
        if i ==0:
            j=0
            q=4
        else:
            j=1
            q=5
        while j<q:
    #    for j in range(len(event_list)):
            #print(j)
            device_nick=event_list[j].offspring("com.bosma.smarthome:id/tvCommonCenterListItemDeviceNick")
            #快速预览播放
            event_list[j].click()
            k=1
            while k==1:
                if poco("com.bosma.smarthome:id/ivCommonVideoRenderLoadingCircleOutSide").exists():
                    print("还在加载")
                    sleep(2)
                else:
                    break
            #poco("com.bosma.smarthome:id/ivCommonVideoRenderLoadingCircleOutSide").click()

            #if poco("com.bosma.smarthome:id/ivCommonVideoRenderLoadingCircleOutSide").exists():
               # print("等待了10s，视频未加载成功")
            #else:
                #video_play=poco("com.bosma.smarthome:id/tvCommonCurrentVideoPlayWay")
                #video_play_way=video_play.attr("text")
            if poco("com.bosma.smarthome:id/tvCommonPlayBackVideoRenderContainerOffline").exists() or poco("com.bosma.smarthome:id/tvCommonCloudPlaybackVideoRenderContainerOffline").exists():
                sleep(2)
                video_play=poco("com.bosma.smarthome:id/tvCommonCurrentVideoPlayWay")
                video_play_way=video_play.attr("text")
                print(video_play_way)

                if video_play_way=="Local":
                    local_offline=poco("com.bosma.smarthome:id/tvCommonPlayBackVideoRenderContainerOffline")
                    local_errorcode=poco("com.bosma.smarthome:id/tvPlayBackVideoRenderContainerOfflineErrorCode")
                    print(f'回放{device_nick.attr("text")}设备的本地视频，回放失败，失败原因：{local_offline.attr("text")};错误码是：{local_errorcode.attr("text")}')
                elif video_play_way=="Cloud":
                    cloud_offline=poco("com.bosma.smarthome:id/tvCommonCloudPlaybackVideoRenderContainerOffline")
                    cloud_errorcode=poco("com.bosma.smarthome:id/tvCommonCloudPlaybackVideoRenderContainerOfflineErrorCode")
                    print(f'回放{device_nick.attr("text")}设备的本地视频，回放失败，失败原因：{cloud_offline.attr("text")};错误码是：{cloud_errorcode.attr("text")}')
                else:
                    print("发生未知错误，请等待")
                    sleep(20)
            else:

                print(f'{device_nick.attr("text")}设备的视频，将回放10s')
                sleep(10)
            j=j+1
        sleep(60)
        
        

        poco.swipe([0.9,0.8532], [0.9,0.371])
        sleep(5)

        i=i+1 
    for k in  range(len(event_list)+1):
        poco.swipe([0.9,0.491], [0.9,0.8532])
        sleep(5)        
#事件回放页面回放
def Events_PlayBack():
    poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.bosma.smarthome:id/smHomeSideMenu").offspring("com.bosma.smarthome:id/fl_fragment_container").child("android.widget.LinearLayout").offspring("android.widget.LinearLayout").child("android.widget.RelativeLayout")[1].offspring("com.bosma.smarthome:id/iv_tab_icon").click()
    i=0
    while i<3:



        event=poco("com.bosma.smarthome:id/rcvCommonEventCenterEventListNewEventContainer").offspring("com.bosma.smarthome:id/llItemCommonEventListContainer")
        event_list=list(event)

        #print(event_list)
        if i ==0:
            j=0
            q=4
        else:
            j=1
            q=5

        for k in range(j,len(event_list)):
            sleep(2)
            device_nick=event_list[k].offspring("com.bosma.smarthome:id/tvCommonCenterListItemDeviceNick")
            device_name=device_nick.attr("text")
            event_list[k].child("com.bosma.smarthome:id/ivItemCommonEventListDetail").click()

            kk=1
            while kk==1:
                if poco("com.bosma.smarthome:id/ivCommonVideoRenderLoadingCircleOutSide").exists():
                    print("还在加载")
                    sleep(2)
                else:
                    break
            if poco("com.bosma.smarthome:id/tvCommonPlayBackVideoRenderContainerOffline").exists() or poco("com.bosma.smarthome:id/tvCommonCloudPlaybackVideoRenderContainerOffline").exists():
                sleep(2)
                video_play=poco("com.bosma.smarthome:id/tvCommonCurrentVideoPlayWay")
                video_play_way=video_play.attr("text")
                print(video_play_way)

                if video_play_way=="Local":
                    local_offline=poco("com.bosma.smarthome:id/tvCommonPlayBackVideoRenderContainerOffline")
                    local_errorcode=poco("com.bosma.smarthome:id/tvPlayBackVideoRenderContainerOfflineErrorCode")
                    print(f'回放{device_name}设备的本地视频，回放失败，失败原因：{local_offline.attr("text")};错误码是：{local_errorcode.attr("text")}')
                    poco("com.bosma.smarthome:id/ibtCommonPlayBackVideoToolBarPortraitClose").click()

                elif video_play_way=="Cloud":
                    cloud_offline=poco("com.bosma.smarthome:id/tvCommonCloudPlaybackVideoRenderContainerOffline")
                    cloud_errorcode=poco("com.bosma.smarthome:id/tvCommonCloudPlaybackVideoRenderContainerOfflineErrorCode")
                    print(f'回放{device_name}设备的本地视频，回放失败，失败原因：{cloud_offline.attr("text")};错误码是：{cloud_errorcode.attr("text")}')
                    poco("com.bosma.smarthome:id/ibtCommonPlayBackVideoToolBarPortraitClose").click()

                else:
                    print("发生未知错误，请等待")
                    sleep(20)
                    poco("com.bosma.smarthome:id/ibtCommonPlayBackVideoToolBarPortraitClose").click()
            else:

                print(f'{device_name}设备的视频，将回放10s')
                sleep(20)

                poco("com.bosma.smarthome:id/ibtCommonPlayBackVideoToolBarPortraitClose").click()

        poco.swipe([0.9,0.8532], [0.9,0.371])
        sleep(5)

        i=i+1 

    for k in  range(len(event_list)+1):
        poco.swipe([0.9,0.491], [0.9,0.8532])
        sleep(5)
        
#事件查询
def Events_date_Search(day=3):
    #查询前三天的事件
    for i in range(day):

        poco("com.bosma.smarthome:id/ivToolbarRightIcon").click()
        poco("com.bosma.smarthome:id/ivEventConditionFilterDate").click()


        sleep(3)

        poco.swipe((0.8187,0.499),(0.8187,0.56))
        sleep(3)
        poco("com.bosma.smarthome:id/btnDateSelectedDialogRight").click()

        poco("com.bosma.smarthome:id/tvToolbarRightContent").click()
        date=poco("com.bosma.smarthome:id/tvToolbarTitle").attr("text")

        if poco("com.bosma.smarthome:id/ivCommonEventCenterEventListNewNoData").exists():
            print(f'查询{date}的事件,当天没数据')

        elif  poco("com.bosma.smarthome:id/ivCommonEventListItemEventPlay").exists():
            print(f'查询{date}的事件,当天有数据')
        else:
            print(f'查询{date}的事件,查询异常')
            sleep(10)
        sleep(3)
    #切回今天
    poco("com.bosma.smarthome:id/ivToolbarRightIcon").click()
    poco("com.bosma.smarthome:id/ivEventConditionFilterDate").click()
    sleep(3)
    for j in range(day):
        
        poco.swipe((0.8187,0.499),(0.8187,0.438))
        sleep(3)
    poco("com.bosma.smarthome:id/btnDateSelectedDialogRight").click()
    poco("com.bosma.smarthome:id/tvToolbarRightContent").click()

    #查询未来日期
    print("查询未来日期")
    poco("com.bosma.smarthome:id/ivToolbarRightIcon").click()
    poco("com.bosma.smarthome:id/ivEventConditionFilterDate").click()
    poco.swipe((0.8187,0.499),(0.8187,0.438))
    
    poco("com.bosma.smarthome:id/btnDateSelectedDialogRight").click()
    backup=poco("com.bosma.smarthome:id/tvDialogContent")
    print(f'查询失败:{backup.attr("text")}')
    poco("com.bosma.smarthome:id/btnDialogOk").click()
    poco("com.bosma.smarthome:id/tvToolbarRightContent").click()
    
#设备查询               
def Event_Devices_Search():

    poco("com.bosma.smarthome:id/ivToolbarRightIcon").click()
    devices_container=poco("com.bosma.smarthome:id/rcvEventConditionFilterDeviceContainer").offspring("android.widget.LinearLayout")
    devices_container_list=list(devices_container)
    #print(f'共有{len(devices_container_list)}个设备')


    for i in range(len(devices_container_list)-1):

        device_name=devices_container_list[i].offspring("com.bosma.smarthome:id/tvItemCommonLabelTip")

        devices_container_list[i].offspring("com.bosma.smarthome:id/ivItemCommonLabelSrc").click()
        #print (device_name.attr("text"))

    sleep(2)
    poco("com.bosma.smarthome:id/tvToolbarRightContent").click()

    #恢复默认设备选项
    sleep(5)
    poco("com.bosma.smarthome:id/ivToolbarRightIcon").click()
    devices_container=poco("com.bosma.smarthome:id/rcvEventConditionFilterDeviceContainer").offspring("android.widget.LinearLayout")
    devices_container_list=list(devices_container)
    #print(f'共有{len(devices_container_list)}个设备')


    for i in range(len(devices_container_list)-1):

        device_name=devices_container_list[i].offspring("com.bosma.smarthome:id/tvItemCommonLabelTip")

        devices_container_list[i].offspring("com.bosma.smarthome:id/ivItemCommonLabelSrc").click()
        #print (device_name.attr("text"))

    sleep(2)
    poco("com.bosma.smarthome:id/tvToolbarRightContent").click()





Events_PlayBack()
                 
 





            



        






