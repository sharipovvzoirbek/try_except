import os

try:
    os.mkdir("papka")
except FileExistsError:
    print("file mavjud")


file=open('papka/zaby.txt', 'w')
file.write("writed")


try:
    os.mkdir('forfile')
except FileExistsError:
    print("bu ham mavjud")


zed = open('forfile/red.txt','w')
zed.write('deathnote')



try:
    os.mkdir('note')
except FileExistsError:
    print('bunisi ham ')


ded = open('note/text.txt','w')
ded.write('kitob')
