import clr
from time import sleep

'''
author：     王海峰 plutohfw@gmail.com
创建时间:     2023/6/14
最后维护时间: 2023/6/14
用python的方法使用UR动态库，这个库比较老旧，可以考虑看我github仓库里的另外一个项目URServer
这里做一个动态库的调用演示，请足够了解UR的remote control再来研究这个SDK
dll文件由ur中国提供，dll created by universal-robots China
'''

clr.AddReference("D:\\backup\\UR_dll\\URSDK-PC\\URSDK_V3_1.dll") #使用绝对路径
from URSDK.RobController.Communication import *
# from URSDK.RobController.Datatype import *
if __name__ == "__main__":
    DashBoard = DashBoard("192.168.168.129",29999)
    P=PrimaryInterface("192.168.168.129",30001)
    # primaryInt=PrimaryInterface("192.168.168.129",30001)
    # DashBoard.poweron()
    DashBoard.brakerelease()
    # DashBoard.poweroff()

    print(P.startPrimary())

    send_data = f'''
def whf():
    popup("success")
end
    '''
    P.sendScript(send_data)
    # while 1:
    #     print(P.getRobotState().configurationData.controllerBoxType())
    #     sleep(0.5)
