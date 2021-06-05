from turtle import *
reset()
def _forward(ins):
    j=[]
    for i in ins:
        j.append(int(i))
    forward(sum(j))
def _backward(ins):
    j=[]
    for i in ins:
        j.append(int(i))
    backward(sum(j))
def _right(ins):
    j=[]
    for i in ins:
        j.append(int(i))
    right(sum(j))
def _left(ins):
    j=[]
    for i in ins:
        j.append(int(i))
    left(sum(j))
def _penup(ins):
    penup()
def _pendown(ins):
    pendown()
def _reset(ins):
    reset()
comms={'F':_forward,'B':_backward,'R':_right,'L':_left,'U':_penup,'D':_pendown,'RE':_reset}
def code(code):
    global comms
    codes=code.split('|')
    for i in codes:
            sub_codes=i.split(':')
            try:
                inputs=sub_codes[1].split('+')
            except IndexError:
                inputs=[]
            if sub_codes[0] in comms:
                try:
                    for i in range(int(sub_codes[2])):
                        comms[sub_codes[0]](inputs)
                except IndexError:
                    comms[sub_codes[0]](inputs)
while True:
    code(input())
