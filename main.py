#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-21 下午5:12
# @Author  : Aries
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import werobot


robot = werobot.WeRoBot(token='gabrielhan')


@robot.text
def hello_world():
    return 'Hello World!'

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
