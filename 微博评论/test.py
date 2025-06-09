import re
s = "我是<a href='/n/重庆共青团'>@重庆共青团</a>  ，我在重庆，和青年朋友们一起文化跨年！祝大家新年快乐！  "

print(s.index('s'))
a = re.findall("<a.*</a>", s)[0]
b = re.findall(">@(.*?)</a>", s)[0]
s = s.replace(a, b)
print(a)
print(b)
print(s)