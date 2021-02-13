import socket
from datetime import datetime

def encode(string):
    result=''
    for char in string:
        result+=hex(ord(char))[2:]
        result+='_'
    return result[:-1]

def decode(string):
    result=''
    splited=string.split('_')
    for code in splited:
        int_code=int(code,base=16)
        result+=chr(int_code)
    return result

def getmyip(host=socket.gethostname()):
    return socket.gethostbyname(host)

class Person:
    def __init__(self,**data):
        self.name=decode(data['name'])
        self.ip=decode(data['ip'])

class Msg:
    def __init__(self,**data):
        self.person=data['person']
        self.messag=decode(data['messag'])
        self.time=decode(data['time'])
    def format(self,who):
        t=who.replace('{person}',self.person.name)
        t=t.replace('{messag}',self.messag)
        t=t.replace('{time}',self.time)
        return t

def now():
    nowdate=datetime.now()
    return nowdate.strftime("%H:%M:%S %d.%m.%Y")

def writetochat(**data):
    ip=encode(data['ip'])
    msg=encode(data['msg'].replace('\n','<br>').replace('$IP',decode(ip)))
    name=encode(data['name'].replace('$IP',decode(ip)))
    time=encode(data['time'])
    txt=f'Msg(person=Person(name="{name}",ip="{ip}"),messag="{msg}",time="{time}")'
    f=open('chatishe.txt','a')
    print(txt,file=f)
    f.close()

CSS_SUBMIT_RESET='''
.btn {
    border: none; /* Remove borders */
    color: white; /* Add a text color */
    padding: 14px 28px; /* Add some padding */
    cursor: pointer; /* Add a pointer cursor on mouse-over */
}

input[type=submit] {display: none;}
input[type=reset] {display:none;}

i {width:48px;height:48px;}

.bg-blue {background-color: #2196F3;}
.bg-blue:hover {background: #0b7dda}

.bg-red {background-color: #f44336;}
.bg-red:hover {background: #da190b;}

'''

CSS_CHANGE='''
/* The switch - the box around the slider */
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

/* Hide default HTML checkbox */
.switch input {display:none;}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
'''

CSS_TEXTAREA='''
textarea {
border:none;
background-color:#d3d3d3;
}
input[type=text] {
border:none;
background-color:#d3d3d3;
}
'''

CSS_CHAT='''
/* Chat containers */
.container {
    border: 2px solid #dedede;
    background-color: #f1f1f1;
    border-radius: 5px;
    padding: 10px;
    margin: 10px 0;
}

/* Darker chat container */
.darker {
    border-color: #ccc;
    background-color: #ddd;
}

/* Clear floats */
.container::after {
    content: "";
    clear: both;
    display: table;
}

/* Style names */
.container h6 {
    float: left;
    max-width: 60px;
    width: 100%;
    margin-right: 20px;
}

/* Style the right name */
.container h6.right {
    float: right;
    margin-left: 20px;
    margin-right:0;
}

/* Style time text */
.time-right {
    float: right;
    color: #aaa;
}

/* Style time text */
.time-left {
    float: left;
    color: #999;
'''
NOT_ME='''<div class="container">
  <h6>{person}</h6>
  <p>{messag}</p>
  <span class="time-right">{time}</span>
</div>'''
ME='''<div class="container darker">
  <h6 class="right">{person}</h6>
  <p>{messag}</p>
  <span class="time-left">{time}</span>
</div>'''

SCRIPT_FMSR='''
function fmsubmit(){document.getElementById("s").click();}
function fmreset(){document.getElementById("r").click();}
'''
