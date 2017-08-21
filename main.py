#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-21 下午5:12
# @Author  : Aries
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import werobot
import secret


robot = werobot.WeRoBot(token='gabrielhan')


@robot.text
def hello_world():
    return 'Hello World!'

robot.config['APP_ID'] = secret.APP_ID
robot.config['APP_SECRET'] = secret.APP_SECRET
robot.config['ENCODING_AES_KEY'] = secret.ENCODING_AES_KEY
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
