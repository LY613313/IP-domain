import requests
import re
import json
import tldextract
import urllib3
import module.randagent as randagent
import openpyxl as op
from urllib.parse import urlparse
from module.ipjudgment import isIpVsAddrLegal
from colorama import Fore, Back, Style
from module.gettime import nowtime

urllib3.disable_warnings() # 禁止https告警


def apiget(ip):
    # 随机获取user-agent
    headers = randagent.get()
    url = 'https://api.webscan.cc/?action=query&ip=' + ip
    res = requests.get(url,headers = headers)
    res_list = json.loads(res.text)
    # print(res_list)
    return res_list


# 处理api查询结果
def resdispose(list):
    domain = []
    fulldomain = []
    title = []
    if list == None:       
        # print(Fore.YELLOW + nowtime() + " There is no domain name to resolve")
        pass
    else:
        for i in list:
            if isIpVsAddrLegal(i['domain']) == False:
                full_domain = i['domain']
                fulldomain.append(full_domain)
                domain_value = Domainextract(full_domain)
                # fulldomain.append(full_domain)
                domain.append(domain_value)
                title_value = i['title']
                title.append(title_value)
                # print(domain)
                # print(fulldomain)
                # print(title)
        return domain,fulldomain,title


# 域名提取
def Domainextract(domain):
    strlist = domain.split('.')
    return strlist[-2] + '.' + strlist[-1]


def storagedate():
    value = [] # 
    num = 1
    with open('ip.txt',encoding='utf8') as f:
        f = list(set(f))
        for i in f:
            ip = i.strip()
            # print(type(ip))
            res = apiget(ip)
            if resdispose(res) != None:
                domain,fulldomain,title = resdispose(res)
                # print(domain,fulldomain,title)
                for j in range(len(domain)):
                    data = []
                    print(Fore.YELLOW + nowtime() + " \033[32mThe IP of \033[0m" + ip + " \033[32mresolves domain is \033[0m",end='')
                    print(list((num,ip,fulldomain[j],domain[j],title[j])))
                    # print(type(list((num,ip,fulldomain[j],domain[j],title[j]))))
                    # data = data.extend(list((num,ip,fulldomain,domain,title)))
                    # print(type(data))
                    value.append(list((num,ip,fulldomain[j],domain[j],title[j])))
                    num += 1
            else:
                print(Fore.YELLOW + nowtime() + " \033[31mThere is no domain name to resolve of IP: \033[0m" + ip)
    return value


def excelstorage(list,filename):
    wb = op.Workbook()  # 创建工作簿对象
    ws = wb['Sheet']  # 创建子表
    ws.append(['序号', 'ip', '全域名','域名','标题'])
    for i in list:
        d = i[0],i[1],i[2],i[3],i[4]
        ws.append(d)
    wb.save(filename)


def main():
    print(Fore.YELLOW + nowtime() + " \033[34mWelcome to use the script of IP address resolves domain.This script was written in 20230924.\033[0m")
    print(Fore.YELLOW + nowtime() + " \033[34mStart to resolves domain. The result of resolves is id,IP,fulldomain,domian,title.\033[0m")
    list = storagedate()
    file_name = input(Fore.YELLOW + nowtime() + "\033[34m Please input the filename to save the result : \033[0m")
    filename = './result/' + file_name
    excelstorage(list,filename)
    print(Fore.YELLOW + nowtime() + " \033[32mSuccess to save the file of :\033[0m" + filename)


if __name__ == "__main__":
    main()

