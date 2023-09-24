# 🥪Readme

```
time : 2023-9-24
author : LY613313
title : IP批量反查域名
```
## 🥙脚本介绍

此脚本使用IP反查域名的API为Webscan查询接口，接口文档如下：

```url
https://www.webscan.cc/api/index.html
```

使用接口如下：

```url
https://api.webscan.cc/?action=query&ip=
```

功能介绍：

- 批量进行IP反查域名
- 对IP解析的域名进行处理（包括全域名与域名）
- 默认对查询的IP进行去重

## 🌯脚本使用

使用脚本时先将要查询的IP放到ip.txt的文件中，然后运行**ip-domain.py**即可，运行命令如下

```bash
python ip-domain.py
```

或

```bash
python3 ip-domain.py
```

示例：

![2023-09-24-21-48-03.png](images\2023-09-24-21-48-03.png)

运行完成后要输入你要保存的文件名，注意是要.xlsx后缀（此脚本保存格式为excel文件）

![2023-09-24-21-50-46.png](images\2023-09-24-21-50-46.png)

运行完成后的结果保存在result的文件夹内，如下：

![2023-09-24-21-51-56.png](images\2023-09-24-21-51-56.png)

---

注：本人菜鸡一只，此脚本是自己没事写着玩，没什么大用处。如果存在什么不足，还请各位大佬指正。

