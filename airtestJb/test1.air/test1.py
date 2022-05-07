__author__ = "Administrator"

from airtest.core.api import *

import os
import time
import datetime
import sys
from time import sleep

package="com.zll.zllwdjtxxl"


w,h=device().get_current_resolution()#获取手机分辨率
starttime = datetime.datetime.now()
a=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '\n'

touch([0.6*w, 0.99*h])#点击打开聊天框
