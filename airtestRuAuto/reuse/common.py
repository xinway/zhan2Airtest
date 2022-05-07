import datetime

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from PIL import Image
import pytesseract

if not cli_setup():
    auto_setup(__file__, logdir='./reuse/log')


# 获取当前时间
def now_time():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return now_time


# 文字识别(需要安装Tesseract4)
def orc_image(file):
    image = Image.open(file)
    text = pytesseract.image_to_string(image, lang='chi_sim', config="--psm 6")
    return text
