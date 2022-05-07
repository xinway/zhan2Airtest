from airtest.core.api import *
from airtest.cli.parser import cli_setup

from reuse.gamereuse import *
from reuse.initialization import *


# 连接设备
# connect_device("Android://127.0.0.1:5037/FIFIMFFEPVAIWCU8")

if not cli_setup():
    auto_setup(__file__, logdir='./suite/test1.air/log')
init_device("Android", ime_method="ADBIME")
w, h = shipei()
print("---------------------------执行第一个脚本----------------------------")
touch(Template(r"tpl1650201067605.png", record_pos=(0.357, 0.183), resolution=(2280, 1080)))
print("---------------------------第一个脚本完成----------------------------")
