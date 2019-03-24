import re
import os

def processN(txt):
    pattern_str=r'[^.\n]([.\n])[^.\n]'
    pattern=re.compile(pattern_str)

    while True:
        matches = re.search(pattern, txt)
        if matches:
            s=matches.start(1)
            e=matches.end(1)
            txt=txt[:s]+'\n\n'+txt[e:]
        else:
            break
    return txt

def fuck(s):
    i=0
    inCodes=False
    while i<len(s):
        # 判断进入代码区
        step=1
        try:
            if s[i:i+3]=='```' and not inCodes:
                inCodes=True
                # print('in')
                i=i+1
                continue
        except:pass
        # 单个回车符转换为两个回车符
        if not inCodes:
            if s[i]=='\n' and i+1<len(s) and s[i+1]!= '\n':
                s=s[:i]+'\n\n'+s[i+1:]
                step=2
        # 判断离开代码区
        try:
            if s[i:i+3]=='```' and inCodes:
                inCodes=False
                # print('out')

        except:pass
        i=i+step
    return  s

def process(filename):
    txt=''
    with open('md/'+filename, 'r') as f:
        txt=f.read()
    txt=txt.replace('@[toc]','\n')
    txt=fuck(txt)
    with open('md2/'+filename, 'w') as f:
        f.write(txt)



if __name__ == '__main__':
    for root, dirs, files in os.walk('md'):
        for file in files:
            process(f'{file}')
            prefix=file.split('.')[0]
            cmd=rf'pandoc  -f markdown -t docx md2/{file} -o docx/{prefix}.docx'
            os.system(cmd)
            # break
        break