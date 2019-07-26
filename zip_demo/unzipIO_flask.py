# -*- coding: utf-8 -*-
import flask
import io
import zipfile

app = flask.Flask(__name__)
app.secret_key = "MAOCATZK@GMAIL.COM"

@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        _file = flask.request.files.get("file")
        byteIO = io.BytesIO(_file.read())
        zfile = zipfile.ZipFile(byteIO)
        # 读取zip中的文件 todo：尚未测试zip中的目录
        files = []
        for i in zfile.filelist:
            files.append((i.filename, zfile.read(i.filename))) # zfile.read() 返回二进制数据
        print files
    return '''
             <form method="post" enctype="multipart/form-data">
                <input type="file" name="file">
                <input type="submit" value="提交">
            </form>
        '''


if __name__ == "__main__":
    app.run(port=3001,host='0.0.0.0', debug=True)