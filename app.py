"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Project    : Flask and Swagger Test
# @File    : app.py
# @Time    : 2025/5/3
# @Author  : RJ
————————————————
登录功能包含：
1. 首页路由
2. 登录表单展示
3. 登录验证逻辑
正确凭证：用户名 RJ / 密码 123456
"""

from flask import Flask, render_template, request
from flasgger import Swagger, swag_from

app = Flask(__name__)

# 配置 Flasgger
app.config['SWAGGER'] = {
    'title': '用户认证 API',
    'description': '一个简单的用户登录系统',
    'version': '1.0.0',
    'uiversion': 3,
    'specs_route': '/api/docs/'
}
swagger = Swagger(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    """首页
    ---
    tags:
      - 首页
    responses:
      200:
        description: 返回主页
        content:
          text/html:
            schema:
              type: string
              example: '<html>主页内容</html>'
    """
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    """登录表单页面
    ---
    tags:
      - 认证
    summary: 显示登录表单
    description: 返回包含用户名和密码输入框的表单页面
    responses:
      200:
        description: 返回登录表单
        content:
          text/html:
            schema:
              type: string
              example: '<html>表单内容</html>'
    """
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    """用户登录接口
    ---
    tags:
      - 认证
    summary: 处理用户登录
    description: 验证用户名和密码（正确凭证：RJ/123456）
    consumes:
      - application/x-www-form-urlencoded
    produces:
      - text/html
    parameters:
      - name: username
        in: formData
        type: string
        required: true
        description: 用户名
        example: RJ
      - name: password
        in: formData
        type: string
        required: true
        description: 密码
        example: "123456"
    responses:
      200:
        description: 登录成功
        content:
          text/html:
            schema:
              type: string
              example: '<html>欢迎页面</html>'
      401:
        description: 用户名或密码错误
        content:
          text/html:
            schema:
              type: string
              example: '<html>错误信息</html>'
    """
    username = request.form['username']
    password = request.form['password']
    if username == 'RJ' and password == '123456':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='用户名或密码错误', username=username)

if __name__ == '__main__':
    app.run(debug=True)