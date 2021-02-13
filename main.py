from flask import *
from chat import *
import re,os
app = Flask(__name__)
@app.route('/')
def root():
    f=open("chatishe.txt")
    chat=f.readlines()
    f.close()
    content='<meta charset="utf-32">'
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
    return content+'''<br><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>'''+CSS_TEXTAREA+CSS_SUBMIT_RESET+CSS_CHANGE+'''</style>
<form action="/save/">
<script>
'''+SCRIPT_FMSR+'''
</script>
Имя:<input type=text name="name"><br>
Сообщение:<textarea name=msg></textarea><br>
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
@app.route('/write/')
def write():
    return '<h1 style="font-size:500px;color:orange;>☢error</h1>',301

@app.route('/save/')
def save():
    name=request.args.get('nameip',default=request.args.get('name',default='Аноним')+'H')
    if name.endswith('H'):
        name=re.sub('H$','',name)
    else:
        name=request.args.get('ip')
    time=now()
    writetochat(name=name,msg=request.args.get('msg'),ip=request.args.get('ip'),time=time)
    return redirect('/')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=os.environ.get("PORT", 5000))
