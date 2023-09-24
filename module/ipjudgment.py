# 此函数用于检测是否为IP地址
import sys

def isIpVsAddrLegal(ipStr):

    if '.' not in ipStr:  #判断字符串里面有没有.
        return False

    #用.切割ip地址为一个列表
    ip_split_list = ipStr.strip().split('.')

    if len(ip_split_list) != 4: # 切割后列表必须要有四个元素
        return False

    for i in range(4):
        try:
            ip_split_list[i] = int(ip_split_list[i])
        except:
            print("IP invalid for not number: "+ ipStr)  #每个参数必须为数字，否则校验失败
            exit()  #退出，不再判断后续的字符串

        if ip_split_list[i] <= 255 and ip_split_list[i] >= 0:  #每个参数值必须在0-255之间
            pass
        else:
            print("IP invalid: " + ipStr)
            return False

    if int(ip_split_list[0] == 0):  #first 参数 is not 0
        print("ip format wrong")
        exit() #退出，不再判断后续的字符串

    return True