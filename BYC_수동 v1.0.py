from re import A
import time
import os

w='내가' #단어 #사용x
ww='나는'
www='나'

depression=0 #초기점수
wo=1
woo=1
wooo=1

##
def fileopen(data):#공백을 제외한 문자수
 
    with open(data,'r',encoding='UTF8') as file:
    
        text = file.read()
        
        splitdata = text.split()
 
    return splitdata, len(splitdata)
 
def count_character(data):
 
    count = 0
    
    for i in data :
    
        count += len(i)
 
    return  count
 
data,count = fileopen("글을 입력해 주세요.txt")
 
print("공백을 제외한 문자수 : ",count_character(data)) #공백을 제외한 문자수
##
wii=(count_character(data))
print("wii메인:",wii) #메인글수
##-----------------------------------------------------------------------
with open("글을 입력해 주세요.txt", "r", encoding='utf-8') as f:
    line = f.read()
    for i in line.split():
        if i=="나는":
            wo += 1
print(wo)
##-----------------------------------------------------------------------
with open("글을 입력해 주세요.txt", "r", encoding='utf-8') as f:
    line = f.read()
    for i in line.split():
        if i=="내가":
            woo += 1
print(woo)
##-----------------------------------------------------------------------
with open("글을 입력해 주세요.txt", "r", encoding='utf-8') as f:
    line = f.read()
    for i in line.split():
        if i=="나":
            wooo += 1
print(wooo)
##-----------------------------------------------------------------------
print()

main_1=wii/wo
main_2=wii/woo
main_3=wii/wooo

print(main_1)
print(main_2)
print(main_3)

#was=wii/4.5
#print("기준:",was)

if (main_1<50): #지수 측정, 25글자중 1글이상 나오면 1점+
    depression=depression+33.3

if (main_2<50): #지수 측정, 25글자중 1글이상 나오면 1점+
    depression=depression+33.3

if (main_3<50): #지수 측정, 25글자중 1글이상 나오면 1점+
    depresszon=depression+33.3

print("계산중...\n")
time.sleep(1)
print("99.9점이 최고점 입니다.\n")
time.sleep(2)
print("지수:",depression)

if (depression>49):
    print('\033[91m'+"50점 이상입니다. \n 정확한건 아니지만 참고해주세요..")
elif (depression>32):
    print('\033[92m'+"33점 이상입니다. \n 정확한건 아니지만 참고해주세요..")
elif (depression>98):
    print('\033[91m'+"99점 이상입니다. \n 전문의 상담을 추천드립니다.")
else:
    print('\033[94m'+"아무문제 없습니다 :)")

os.system('\033[0m'+ 'pause')