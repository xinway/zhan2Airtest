from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir='./reuse/log')


# 初始化设备
def initdevice():
    pg = "com.ijunhai.aoe"
    stop_app(pg)
    # clear_app(pg)
    start_app(pg)