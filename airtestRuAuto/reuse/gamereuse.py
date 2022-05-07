import calendar

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import os

if not cli_setup():
    auto_setup(__file__, logdir='./reuse/log')

# 当前时间戳
currentTimestamp = str(calendar.timegm(time.gmtime()))


# 适配
def shipei():
    # 获取设备的宽度和高度
    w, h = device().get_current_resolution()
    return w, h
