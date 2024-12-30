---
ID: 50
post_title: >
  使python代码兼容不同操作系统的文件路径
post_name: 'python%e4%b8%8b%e8%b7%a8%e5%b9%b3%e5%8f%b0%e6%93%8d%e4%bd%9c%e6%96%87%e4%bb%b6%e8%b7%af%e5%be%84'
author: Xuan
post_date: 2012-09-12 03:42:54
layout: post
link: 'https://blog.wangxuan.name/2012/09/12/python%e4%b8%8b%e8%b7%a8%e5%b9%b3%e5%8f%b0%e6%93%8d%e4%bd%9c%e6%96%87%e4%bb%b6%e8%b7%af%e5%be%84/'
published: true
tags:
  - python
categories:
  - Knowhow
---
原标题：Python下跨平台操作文件路径

众所周知，Windows 下的路径分隔符为反斜杠"\",而UNIX-like系统下的路径分隔符为正斜杠"/"，这常导致代码跨平台移植时的问题。  
python 设计为一门跨平台的语言，当然可以轻松解决此问题。

首先，python 在不同平台下都可以正确识别以正斜杠为分隔符的路径。如果在程序中只用到程序中预置的路径字符串（比如说指定库的位置），而不涉及从系统获取文件路径，则只要将路径写为正斜杠分隔路径，代码即可跨平台。

但是如果需要使用 `os.path.abspath() os.walk()` 等函数获取路径，python 返回的路径字符串会是操作系统默认格式的路径字符串。这时的解决方法主要有：  
在需要拼接、查找路径分隔符的地方，使用`os.path.sep`来代替显式的'/'或'\\'，该变量依平台不同而不同。  
当然这样写会比较啰嗦，本来只需要`a+'/'+b+'/'+c`就可以的地方，现在就需要写成`a+os.path.sep+b+os.path.sep+c`了。本来直接`filename.split('/')`就可以，现在就得写成`filename.split(os.path.sep)`。  
所以，对于这些操作，使用`os.path`的各种内置函数来操作，会简洁一些，同时也增加代码的可阅读性。比如说，前面的`a+'/'+b+'/'+c`就可以写成`os.path.join(a,b,c)`。相关操作还有：`os.path.split()`等