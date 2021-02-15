from flask import *
from chat import *
import re,os
app = Flask(__name__)
class Var:
    def __init__(self,v):
        self.v=v
    def set(self,v):
        self.v=v
    def get(self):
        return self.v
lck=Var(False)
@app.route("yandex_678a4b246f7010d9.html")
def yandex_webmaster():
    return '''<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    </head>
    <body>Verification: 678a4b246f7010d9</body>
</html>'''
@app.route('/')
def root():
    f=open("chatishe.txt")
    chat=f.readlines()
    f.close()
    content='<meta charset="utf-32"><title>Чатище</title>'
    content+='<style>'+CSS_CHAT+'</style>'
    for messag in chat:
        if messag.strip()=='':
            continue
        data=eval(messag)
        if request.remote_addr==data.person.ip:
            msg_content=data.format(ME)
        else:
            msg_content=data.format(NOT_ME)
        content+=msg_content
    form='''<br><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>'''+CSS_TEXTAREA+CSS_SUBMIT_RESET+CSS_CHANGE+'''</style>
<form action="/save/">
<script>
'''+SCRIPT_FMSR+'''
</script>
Имя:<input type=text name="name"><br>
Сообщение:<textarea name=msg style="width:640;height:480;"></textarea><br>
<input type=hidden value="'''+request.remote_addr+'''" name=ip>
IP вместо имени:
<label class="switch">
  <input type="checkbox" name="nameip">
  <span class="slider"></span>
</label><br>
<input type=submit id=s><input type=reset id=r>
<div style="font-size:48px">
<i class="fa fa-send bg-blue" onclick="fmsubmit();"></i>
<i class="fa fa-trash bg-red" onclick="fmreset();"></i>
</div>
</form>'''
    if lck.get():
        form='<div align="center" style="color:#777;font-size:1.5em;">Чатище отключено :(</div>'
    return content+form

@app.route('/save/')
def save():
    if lck.get():
        abort(403)
    name=request.args.get('nameip',default=request.args.get('name',default='Аноним')+'H')
    if name.endswith('H'):
        name=re.sub('H$','',name)
    else:
        name=request.args.get('ip')
    if name.strip()=='':
        name='Аноним'
    time=now()
    msg=request.args.get('msg','<div style="color:#777">(Пусто)</div>')
    if msg.strip()=='':
        msg='<div style="color:#777">(Пусто)</div>'
    writetochat(name=name,msg=msg,ip=request.args.get('ip','0.0.0.0'),time=time)
    return redirect('/')
@app.route('/admin/')
def admin():
    o=request.args.get('o',None)
    if o is None:
        with open('chatishe.txt') as f:
            c=f.read().strip()
        return f'<form action="/admin"><textarea name=o style="width:640;height:480;">{c}</textarea><input type=submit></form>'
    else:
        if o=='-/-':
            o=''
        with open('chatishe.txt','w') as f:
            f.write(o)
        return redirect('/')
@app.route('/clear/')
def clear():
    with open('chatishe.txt','w') as f:
        f.write('')
    return redirect('/')
@app.route('/toggle/')
def toggle():
    lck.set(not lck.get())
    return redirect('/')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=os.environ.get("PORT", 5000))
