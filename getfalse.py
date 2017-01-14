#encoding=UTF-8
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 在相同文件路径下将需要检查的文件
false = []
string = ''
i = 0
for line in open('./urls.txt'):
    try:
        request = urllib2.Request(line.encode('utf-8'))
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
        response = urllib2.urlopen(request, timeout=100)
        i += 1
        print i
    except Exception, e:
        print line, str(e)
        false.append(line)
for line in false:
        string += line
open('./false_urls.txt','w').write(string)
