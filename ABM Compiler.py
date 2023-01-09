#open file
fpin = open('input.abm', 'r')
fpout = open('compile.out', 'w')

from collections import namedtuple

stack = []      #stack array
command = []    #command array
mapLabel = {}   #label index map(for goto)
link = {}       #

A = ''
B = ''


Pair = namedtuple("Pair", ["first", "second"])


def getPQ(a):
    global A, B
    a = a.lstrip(' ')
    a = a.lstrip('\t')
    if len(a) > 1:
        a = a[:-1]
    else :
        A= ''
        return
    sp = a.split(' ', 1)
    A = sp[0]
    B = '';
    if len(sp) > 1:
        B = sp[1]
    B = B.lstrip(' ')
    B = B.strip(' ')



def run_command(idx, ram, localram):
    global A, B
    if idx >= len(command):
        return;
    com = command[idx]
    getPQ(com)
    p = A
    q = B

    if p == 'push':
        stack.append(Pair("$", int(q)))
    if p == 'pop':
        stack.pop();
    if p == 'rvalue':
        if q in ram:
            stack.append(Pair(q, ram[q]))
        else:
            stack.append(Pair(q, 0))
    if p == 'lvalue':
        stack.append(Pair(q, int(0)))
        localram[q] = 0
    if p == ':=':
        r = stack.pop()
        l = stack.pop()
        ram[l.first] = r.second
        localram[l.first] = r.second
    if p == 'copy':
        stack.append(stack[-1]);

    if p == 'goto':
        run_command(mapLabel[q], ram, localram)
        return;
    if p == 'gofalse':
        logicState = (stack.pop()).second
        if logicState == 0:
            run_command(mapLabel[q], ram, localram)
            return
    if p == 'gotrue':
        logicState = (stack.pop()).second
        if logicState != 0:
            run_command(mapLabel[q], ram, localram)
            return
    if p == 'halt':
        return

    if p == '+':
        r = (stack.pop()).second
        l = (stack.pop()).second
        stack.append(Pair('$', l + r));
    if p == '-':
        r = (stack.pop()).second
        l = (stack.pop()).second
        stack.append(Pair('$', l - r));
    if p == '*':
        r = (stack.pop()).second
        l = (stack.pop()).second
        stack.append(Pair('$', l * r));
    if p == '/':
        r = (stack.pop()).second
        l = (stack.pop()).second
        stack.append(Pair('$', int(l / r)));
    if p == 'div':
        r = (stack.pop()).second
        l = (stack.pop()).second
        stack.append(Pair('$', l % r));
    if p == '&':
        r = (stack.pop()).second
        l = (stack.pop()).second
        stack.append(Pair('$', l & r));
    if p == '|':
        r = (stack.pop()).second
        l = (stack.pop()).second
        stack.append(Pair('$', l | r));
    if p == '!':
        l = (stack.pop()).second
        stack.append(Pair('$', not(l)));

    if p == '<>':
        r = (stack.pop()).second
        l = (stack.pop()).second
        stack.append(Pair('$', l != r));
    if p == '<':
        r = (stack.pop()).second
        l = (stack.pop()).second
        stack.append(Pair('$', l < r));
    if p == '>':
        r = (stack.pop()).second
        l = (stack.pop()).second
        stack.append(Pair('$', l > r));
    if p == '<=':
        r = (stack.pop()).second
        l = (stack.pop()).second
        stack.append(Pair('$', l <= r));
    if p == '>=':
        r = (stack.pop()).second
        l = (stack.pop()).second
        stack.append(Pair('$', l >= r));
    if p == '=':
        r = (stack.pop()).second
        l = (stack.pop()).second
        stack.append(Pair('$', l = r));

    if p == 'print':
        fpout.write(str(stack[-1].second) + '\n')
    if p == 'show':
        fpout.write(q + '\n')
    if p == 'call':
        emptyram = {}
        run_command(mapLabel[q], localram, emptyram)
        for t in localram:
            if t in ram:
                ram[t] = localram[t]
    if p == 'return':
        return
    if p == 'begin':
        emptyram = {}
        nram = {}
        for t in ram:
            nram[t] = ram[t]
        run_command(idx + 1, nram, emptyram)
        for t in nram:
            if t in ram:
                ram[t] = nram[t]        
        run_command(link[idx], ram, localram)
        return
    if p == 'end':
        return
    
    run_command(idx+1, ram, localram)


#reading input data
while True:
    txt = fpin.readline()
    if txt == '':
        break
    command.append(txt)

#hasing label to line and link
lvs = []
for i in range(len(command)):
    getPQ(command[i])
    if A == 'label':
        mapLabel[B] = i + 1
    if A == 'begin':
        lvs.append(i)
    if A == 'end':
        link[lvs.pop()] = i + 1
        
    
#run
ram = {}
localram = {}
run_command(0, ram, localram)

print("ok")

#close file
fpin.close()
fpout.close()
