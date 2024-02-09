# Readme

首先感谢不知名的图片作者制作的精良祝福语图，感谢。侵权必删。

再感谢原神项目组，项目中的字体仅供学习演示，不可商用。

## 简介

一个用来做自动化的，没有薛定谔的用户友好性的，朴素的祝福语添加工具

## 安装 （请自行替换'/'为你所使用的操作系统的分隔符）

请将'projects'替换为你想安装到的目录

```
cd ~/'projects'
git clone https://github.com/Player-MINEPIG/edit_the_New_Year_greeting_image.git
cd ./edit_the_New_Year_greeting_image
pip install -r requirements.txt
```

## 用法

1. 导航到对应文件夹下
   `cd ~/'projects'/edit_the_New_Year_greeting_image`

2. 然后启动程序

   `python edit_the_New_Year_greeting_image.py`

3. 输入你想要放进去的词，可以用空格分割，但是不要多行，也不要用其他字符分割

4. 根据你的词在图的上方添加一行纯色色块并写上“祝”+你的输入+“：”然后输出到'./output'文件夹，重命名为‘处理编号+你的输入+edited_the_New_Year_greeting_image'

- 示例：

  你自己用一下不就知道了？

  看一下代码也行，应该比较好懂的

## 更新说明

添加了json文件，现在不用进代码里面也可以控制原图来源，字体，字的大小，字的颜色，字的位置，色块颜色和色块大小了

更新了代码，令其更加模块化，降低其维护成本
