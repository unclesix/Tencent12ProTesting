import allure
import pytest

def test_attach_txt():
    allure.attach("这是一个纯文本信息",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段htmldoby块</body>","html测试块",attachment_type=allure.attachment_type.HTML)

#注意图片要以file方法
def test_attach_image():
    allure.attach.file("D:\mylearntest\datas\微信图片_20200611185933.jpg",name="这是一个图片",attachment_type=allure.attachment_type.JPG)
