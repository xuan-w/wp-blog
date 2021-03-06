---
ID: 34
post_title: WORD2007中文版翻译BUG一枚
post_name: 'word2007%e4%b8%ad%e6%96%87%e7%89%88%e7%bf%bb%e8%af%91bug%e4%b8%80%e6%9e%9a'
author: Xuan
post_date: 2010-06-03 05:41:12
layout: post
link: 'https://blog.wangxuan.name/2010/06/03/word2007%e4%b8%ad%e6%96%87%e7%89%88%e7%bf%bb%e8%af%91bug%e4%b8%80%e6%9e%9a/'
published: true
tags:
  - Microsoft Word
  - Word Processing
  - 文字处理
categories:
  - Facts
  - Knowhow
  - Writing Tools
---
波浪线下面一个等号，“≅”，这个符号转义符是`\cong`，即 congruence 的简写，也就是说这是全等号

但是在 Word 2007 的公式编辑器中，鼠标移到这个符号上面，会显示“约等于”！这可以算是一个中译的BUG了。

下面的几个算是译得不准：  
约等于号`\approx` “≈” 被 Word 说成是“几乎等于（渐近于）”，好吧，这个解释也不算错。  
而相似符号`\sim` “∼”却被 Word 说是“约等于号”，雷啊！  
`\simeq`，“≃”，Word 说是“渐近等于”

2020年4月更新：

经过查证，这并不是一个中文翻译错误。因为英文版 Word 里本来就是错的！

而微软犯这个错的原因是，Unicode 标准里对这些符号的解释就是错的，和数学家常用的意义不同。虽然另一个 ISO 标准中使用了正确的解释，但显然微软使用的 Unicode 解释。

对此的辨析见

<https://math.stackexchange.com/questions/507609/when-to-use-congruent-vs-approximately>