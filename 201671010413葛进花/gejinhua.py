import re #应用re模块

lines_count = 0
chars_count = 0
words_dict= {}

f=open('cyy.txt','r')

for line in f:
    lines_count = lines_count + 1
    chars_count  = chars_count + len(line)
    match = re.findall(r'[^a-zA-Z]+', line)#匹配英文单词
    for i in match:
        line = line.replace(i, ' ')
        lines_list = line.split()
    for i in lines_list:
        if i not in words_dict:
            words_dict[i] = 1
        else:
            words_dict[i] = words_dict[i] + 1
f.close()

for w,n in words_dict.items():
    n=min
    print(w,n)

