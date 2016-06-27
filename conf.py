# -*- coding: UTF-8 -*
start = '001'
end = '010'
url = 'http://roll.news.sina.com.cn/s/channel.php?page=%s'
dir = 'part1'

def addZero(l,num):
    while True:
        if(len(num))>=l:
            break
        num = '0'+num
    return num

if __name__ == '__main__':
    for i in range(int(start),int(end)+1):
        print url.replace('%s',addZero(len(start),str(i)))