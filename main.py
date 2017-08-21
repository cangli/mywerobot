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

robot.config['APP_ID'] = 'wxf31a6c50bf4b7a07'
robot.config['APP_SECRET'] = '9f513338d0611a633750afb981d20a5c'
robot.config['ENCODING_AES_KEY'] = 'U4lCzGqRK0ExAsWoqjouEu4qO42qLLJkeDuMjauaVZg'
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
