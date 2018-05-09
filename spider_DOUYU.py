import re
import requests
import os
result = requests.get('https://www.douyu.com/')
html = result.text
imgList = re.findall('data-original="(.*?\.(jpg|png))"',html)
#print(imgList)
j = 1
if not os.path.exists('images'):
    os.mkdir('images')
for i in imgList:
    #print(i[0])
    response = requests.get(i[0])
    with open('./images/%d.png'%j,'wb') as file:
        file.write(response.content)
    j+=1
    print(j)

