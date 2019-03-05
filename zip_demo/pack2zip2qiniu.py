# -*- coding: utf-8 -*-
# python2
'''
    requests 请求服务器资源打包进zip上穿到七牛yun
    纯IO里进行
'''

import requests
from qiniu import Auth, put_data
import io
import zipfile

QINIU_AK = ''
QINIU_SK = ''
q = Auth(QINIU_AK, QINIU_SK)
# url image
url = "https://avatars1.githubusercontent.com/u/37769031?s=460&v=4"
file_name = url.split("/")[-1].split("?")[0]
# 七牛处理加密文件url
# url = q.private_download_url(url, expires=300)
pic = requests.get(url)

bucket = 'demo'
full_filename = "上传的zip.zip"
file_io = io.BytesIO(pic.content)
file_io.seek(0)
buffer = io.BytesIO()

zfile = zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED, allowZip64=False)
zfile.writestr(file_name +'.jpg', file_io.getvalue())
zfile.close()
buffer.seek(0)
token = q.upload_token(bucket,
                       full_filename, 36000)
ret, info = put_data(token, full_filename, buffer.read())
print '{}{}?t={}'.format(
    'pmr318jrz.bkt.clouddn.com/', ret['key'].encode("utf-8"), 111)
