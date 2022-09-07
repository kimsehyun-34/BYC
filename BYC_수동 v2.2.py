from re import A
import time
import os

w='내가' #단어 #사용x
ww='나는'
www='나'
wwww='내'
wwwww='난'
o="우리"

depression=0 #초기점수
wo=1
woo=1
wooo=1
woooo=1
wooooo=1
io=1

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
print("나는.. :",wo)
##-----------------------------------------------------------------------
with open("글을 입력해 주세요.txt", "r", encoding='utf-8') as f:
    line = f.read()
    for i in line.split():
        if i=="내가":
            woo += 1
print("내가.. :",woo)
##-----------------------------------------------------------------------
with open("글을 입력해 주세요.txt", "r", encoding='utf-8') as f:
    line = f.read()
    for i in line.split():
        if i=="나":
            wooo += 1
print("나.. :",wooo)
##-----------------------------------------------------------------------
with open("글을 입력해 주세요.txt", "r", encoding='utf-8') as f:
    line = f.read()
    for i in line.split():
        if i=="내":
            woooo += 1
print("내.. :",woooo)
##-----------------------------------------------------------------------
with open("글을 입력해 주세요.txt", "r", encoding='utf-8') as f:
    line = f.read()
    for i in line.split():
        if i=="난":
            wooooo += 1
print("난.. :",wooooo)
##-----------------------------------------------------------------------
with open("글을 입력해 주세요.txt", "r", encoding='utf-8') as f:
    line = f.read()
    for i in line.split():
        if i=="우리":
            io += 1
print("우리.. :",io)
##-----------------------------------------------------------------------
print()

main_1=wii/wo
main_2=wii/woo
main_3=wii/wooo
main_4=wii/woooo
main_5=wii/wooooo
mainp=wii/io

print("1:",main_1)
print("2:",main_2)
print("3:",main_3)
print("4:",main_4)
print("5:",main_5)
print("+1:",mainp)

#was=wii/4.5
#print("기준:",was)

if (main_1<55): #지수 측정, x글자중 1글이상 나오면 33.3점+
    depression=depression+20.5
    if (main_1<35):
        depression=depression+20

if (main_2<55): #지수 측정, x글자중 1글이상 나오면 33.3점+
    depression=depression+20.5
    if (main_2<35):
        depression=depression+20

if (main_3<55): #지수 측정, x글자중 1글이상 나오면 33.3점+
    depression=depression+20.5
    if (main_3<35):
        depression=depression+20

if (main_4<55): #지수 축정, x글자중 1글상 니오면 18점+
    depression=depression+18
    if (main_4<15):
        depression=depression+15

if (main_5<55):
    depression=depression+20.5
    if (main_5<35):
        depression=depression+20

if (io>2): #다인칭 대명사 사용시 개수만큼 지수를 차함
    iio=(io-1)*2
    depresszon=depresszon-iio
    

print("\n계산중...\n")
time.sleep(1)
print("195점 이 최고점 입니다.\n")
time.sleep(2)
print()
print('\033[96m'+"--------------------")
print('\033[93m'+"지수:",depression)
print('\033[96m'+"--------------------")
print()

if (depression>49):
    print('\033[91m'+"50점 이상입니다. \n\n정확한건 아니지만 참고해주세요..")
elif (depression>19):
    print('\033[92m'+"20점 이상입니다. \n\n정확한건 아니지만 참고해주세요..")
elif (depression>98):
    print('\033[91m'+"99점 이상입니다. \n\n전문의 상담을 추천드립니다.")
elif (depression>119):
    print('\033[91m'+"120점 이상입니다. \n\n전문의 상담을 추천드립니다.")
else:
    print('\033[92m'+"아무문제 없습니다 :)")

print()
print('\033[96m'+"--------------------"+'\033[0m')
print()
os.system('pause')