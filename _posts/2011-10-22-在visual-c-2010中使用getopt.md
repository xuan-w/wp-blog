---
ID: 56
post_title: 在Visual C++ 2010中使用getopt
post_name: '%e5%9c%a8visual-c-2010%e4%b8%ad%e4%bd%bf%e7%94%a8getopt'
author: Xuan
post_date: 2011-10-22 12:32:33
layout: post
link: 'http://blog.wangxuan.name/2011/10/22/%e5%9c%a8visual-c-2010%e4%b8%ad%e4%bd%bf%e7%94%a8getopt/'
published: true
tags:
  - C++
  - Visual C++
categories:
  - Knowhow
---
getopt是UNIX和Glibc下的一个十分有用的东西。但是因为并未列入C和C++标准，所以Visual C++并不支持\#include\<getopt.h\>。 
那么，希望使用嵌有getopt.h的源代码，或者在自己的代码中使用getopt()该怎么办呢？

大致来说，你肯定需要搞到一个可以用的getopt.h和getopt.c。最常见的是GNU的实现，但使用它意味着你需要遵守GPL。所以网上也有一些其它的实现。到底使用哪个则由个人喜好决定。

有了源代码之后，你有两种选择，一是将getopt.h和getopt.c加入你的project中。或者你可以将getopt.h列入你的VC include路径中，编译getopt.c并列入你的VC链接库路径中。

在实际配置你的VC时，有两个问题：1是你会发现Glibc中getopt相关的C文件并不止一个；2是编译GNU getopt.c你似乎还需要一些其它的配置。

于是有一个懒人的选择：  
<http://ieng6.ucsd.edu/~cs12x/vc08install/vc08install2.html>   
在此链接中，给出了配置Visual C++ 2008的极其详细的步骤。如果你使用VC2008的话，直接下载此页面的getopt9.zip并按说明配置即可。你就可以将getopt的h和lib加入VC。    
它提供的getopt.c基于GNU的getopt并包含了GLib中和getopt相关的所有东西。tailor.h可以让你顺利地编译出GNU的getopt实现。所以如果你希望直接在你的project中使用getopt，也可以直接把getopt9.zip中的tailor.h，getopt.h，getopt.c加入你的project即可。

 

如果你和我一样使用的是VC2010，那么，就不能完全按照此网页的说明来配置了。它提供的编译好的getopt.lib是使用VC2008编译的。而作为一个Win7+Visual Studio2010用户，我的system32文件夹下没有msvcr80.dll，只有msvcr100.dll。所以如果直接使用它提供的lib，你的程序会无法运行。    
你需要解压getopt9.zip之后，双击src目录下的vcproj文件，打开VC2010，把getopt.h拷到src目录下，然后在debug和Release模式（重要！）下分别编译这个project。不用担心配置问题，suo文件已经配置好了，直接F7 Build就得到你要的lib文件。  
然后按网页说明配置VC。  
其中配置include和lib路径一项，VC2010和2008的设置方法不一样。你需要点击：View-\>Property Manager   
在property manager中展开项目名称-\>Debug\|Win32-\>Microsoft.cpp.win32.user项目，双击，VC++ Directories，然后添加include和library路径。  
同理，在Release\|Win32-\>Microsoft.cpp.win32.user中添加路径。
这样添加的include和library路径影响所有project。

如果只欲调整这一个project的路径，菜单Project-\>properties进行配置。

最后，为了保证你的Linker知道寻找getopt.lib，请按以上方法，进Properties Manager或者Project Properties展开Linker-\>input-\>Additional Dependencies，在其中加入getoptd.lib(debug模式下)和getopt.lib(release模式下)。同上，Properties Manager中的Microsoft.cpp.win32.user影响你的所有project，而Project Properties只影响一个Project。你一定不希望你编译的所有程序都链接了getopt.lib，所以，只在要用到的project里链接就够了。