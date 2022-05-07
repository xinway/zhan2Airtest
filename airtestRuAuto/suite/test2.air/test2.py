from airtest.core.api import *
from airtest.cli.parser import cli_setup
# 连接设备
# connect_device("Android://127.0.0.1:5037/FIFIMFFEPVAIWCU8")

if not cli_setup():
    auto_setup(__file__, logdir='./suite/test2.air/log')

print("---------------------------执行第二个脚本----------------------------")
touch(Template(r"tpl1650201099046.png", record_pos=(0.301, 0.149), resolution=(2280, 1080)))
print("---------------------------第二个脚本完成----------------------------")

