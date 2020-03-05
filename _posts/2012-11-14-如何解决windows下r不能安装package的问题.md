---
ID: 53
post_title: >
  如何解决Windows下R不能安装package的问题
post_name: '%e5%a6%82%e4%bd%95%e8%a7%a3%e5%86%b3windows%e4%b8%8br%e4%b8%8d%e8%83%bd%e5%ae%89%e8%a3%85package%e7%9a%84%e9%97%ae%e9%a2%98'
author: Xuan
post_date: 2012-11-14 21:48:17
layout: post
link: 'https://blog.wangxuan.name/2012/11/14/%e5%a6%82%e4%bd%95%e8%a7%a3%e5%86%b3windows%e4%b8%8br%e4%b8%8d%e8%83%bd%e5%ae%89%e8%a3%85package%e7%9a%84%e9%97%ae%e9%a2%98/'
published: true
tags:
  - R
  - Windows
categories:
  - Knowhow
---
Update in Feb 2020:  
增加了 Windows 10  
此外，此问题在新版 R 中不一定还有，因为安装包可能已经修复了这个问题。

在Win10/Win7/Vista下如果使用标准用户来执行R，常常在试图安装package的时候提示无法写入，从而导致安装失败。

原因：  
R默认安装在C:\Program Files目录，安装的package也存放在C:\Program Files\R\R-2.15.1\library目录下。在Win7/Vista中，C:\Program Files目录是一个受系统保护的目录，Users组只有读取和执行的权限，没有写入权限。为了使旧程序正常运作，Windows会将尝试写入此目录的操作重定向到C:\Users\User\AppData\Local目录下。但是R不支持此重定向（反正它在尝试写入Program Files失败之后，确实问过我要不要把package放到My Documents里，成功写入到My Documents却未成功加载package，后者可能是因为——Win7对注册表也有保护，普通用户下禁止写入HKLM，而重定向到HKCU）



解决方法：

方法一：对于不嫌麻烦的人来说，可以每次启动R的时候都使用管理员权限，这样想干啥就干啥。可以右键R，属性-兼容性选项卡，勾选使用管理员权限运行。

方法二：上述方法有两个讨厌之处：第一，对一个像R这样的普通应用程序赋予管理员权限是不安全的；第二，每次启动R还必须同意授予管理员权限（如果你没有把UAC关掉的话）。第二个方法相对来说一劳永逸：更改library目录的权限。

右键C:\Program Files\R\R-2.15.1\library目录，属性－安全－编辑，对Users组添加“写入”权限，从此就不用担心R无法安装package了。