from time import sleep

S = ' '
for B in [unichr(x) for x in xrange(2500, 2800)]:
    print '\n'*100

    print B*3+S*5+B*3+S*3+B*10+S*9+B*3+S*9+B*3+S*5+B*3+S*3+B*3
    print S+B*3+S*3+B*3+S+S*3+B*3+S*15+B*5+S*8+B*3+S*5+B*3+S*3+B*3
    print S*2+B*3+S*1+B*3+S*2+S*3+B*3+S*14+B*3+S+B*3+S*7+B*3+S*5+B*3+S*3+B*3
    print S*4+B*3+S*4+S*3+B*10+S*6+B*3+S*3+B*3+S*6+B*11+S*3+B*3
    print S*4+B*3+S*4+S*3+B*3+S*12+B*11+S*5+B*3+S*5+B*3+S*3+B*3
    print S*4+B*3+S*4+S*3+B*3+S*11+B*3+S*7+B*3+S*4+B*3+S*5+B*3+S*6
    print S*4+B*3+S*4+S*3+B*10+S*3+B*3+S*9+B*3+S*3+B*3+S*5+B*3+S*3+B*3
    sleep(0.3)

