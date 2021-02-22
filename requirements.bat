@echo off
title requirements_install
echo 正在pip换源至国内清华源。。。
pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple
pause
echo 正在安装所需Python模块
pip install -r ./requirements.txt
pause
echo 安装完成，祝您使用愉快！
pause