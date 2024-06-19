# chương trình này tạo. sử lí ảnh diện rộng

import random
import math

MANG=[]

# tạo ma trân số kích thước 130*230
# for h in range (130):
#     mang=[]
#     for c in range (230):
#         mang.append('4 ')
#     MANG.append(mang)

# đọc dữ liệu file map và sao lưu dữ liệu
a = open ('map.txt','r',encoding='utf8')
dl=a.readlines()
a.close()
for i in dl:
    x=i.strip()
    xx=x.split()
    MANG.append(xx)  
b=open('saoluu3.txt','w',encoding='utf8')
for i in MANG:
    for j in i:
        b.write(j+' ')
    b.write('\n')   
b.close()


   
# các thuận toán sử lí ảnh
# for c in range(1,199):
#         for h in range(1,99):
              # nếu xung quanh điểm này là nước thì thay điểm này là nước... bla bla
#             # if MANG[h][c] == '2' and (MANG[h+1][c] != '2' and MANG[h-1][c] !='2' and MANG[h][c+1] != '2' and MANG[h][c-1] !='2') :
#             #     MANG[h][c] ='2'
#             # if MANG[h][c] == '2' and MANG[h-1][c+1] == '2' and MANG[h-1][c-1] =='2':
#             #     MANG[h-1][c]='2' 
#             # if MANG[h][c] == '3' and MANG[h-1][c+1]=='3':
#             #     MANG[h-1][c]='3' 
#             #     MANG[h][c+1]='3'
#             if MANG[h][c] != '2' and MANG[h-1][c]=='2':
#                 MANG[h][c] ='8'
#             if MANG[h][c] != '2' and MANG[h][c-1]=='2':
#                 MANG[h][c] ='9'
#             if MANG[h][c] != '2' and MANG[h][c+1]=='2':
#                 MANG[h][c] ='10'
#             if MANG[h][c] != '2' and MANG[h+1][c]=='2':
#                 MANG[h][c] ='7'
#             if MANG[h][c] != '2' and MANG[h-1][c]=='2' and MANG[h][c+1] =='2' and MANG[h-1][c+1] == '2':
#                 MANG[h][c] = '16'
#             if MANG[h][c] != '2' and MANG[h-1][c]=='2' and MANG[h][c-1] =='2' and MANG[h-1][c+1] == '2':
#                 MANG[h][c] = '15'
#             if MANG[h][c] != '2' and MANG[h+1][c]=='2' and MANG[h][c+1] =='2' and MANG[h+1][c+1] == '2':
#                 MANG[h][c] = '17'
#             if MANG[h][c] != '2' and MANG[h+1][c]=='2' and MANG[h][c-1] =='2' and MANG[h+1][c-1] == '2':
#                 MANG[h][c] = '18'
#             if MANG[h][c] != '2' and MANG[h+1][c]!='2' and MANG[h][c+1] !='2' and MANG[h+1][c+1] == '2':
#                 MANG[h][c] = '14'
#             if MANG[h][c] != '2' and MANG[h+1][c]!='2' and MANG[h][c-1] !='2' and MANG[h+1][c-1] == '2':
#                 MANG[h][c] = '13'
#             if MANG[h][c] != '2' and MANG[h-1][c]!='2' and MANG[h][c+1] !='2' and MANG[h-1][c+1] == '2':
#                 MANG[h][c] = '11'
#             if MANG[h][c] != '2' and MANG[h-1][c]!='2' and MANG[h][c-1] !='2' and MANG[h-1][c-1] == '2':
#                 MANG[h][c] = '12'
                    
# tạo 1 vùng toàn là gạch
# for h in range(18,37):
#     for c in range(91,118):
#         MANG[h][c]='3'

# copy map 100*200 -> 130*230 ( ví dụ dùng để thêm cây)
# mang=[]
# a = open ('test.txt','r',encoding='utf8')
# dl=a.readlines()
# a.close()
# for i in dl:
#     x=i.strip()
#     xx=x.split()
#     mang.append(xx)

# for c in range(226,230):
#     for h in range(27,30):
#         MANG[h][c]='4'

# tạo ngẫn nhiên trên 1 hình chữ nhật các đối tượng ( đây là cỏ)
# for i in range(5000):
#     h = random.randint(1, 129)
#     c = random.randint(1,229)
#     MANG[h][c]='0'
    
# hàm này để vẽ hình trái tim thì phải
# for i in range(600):
#     t=i/10
#     c=-0.01*(-t**2+40*t+1200)*math.sin(math.pi*t/180)
#     h=-0.01*(-t**2+40*t+1200)*math.cos(math.pi*t/180)
#     c=-int(1.3*(c+0.5))+40
#     h=int(1.3*(h+0.5))+50
#     MANG[h][c]='1'
    
# làm mờ đoạn thẳng
# for h in range(60,75):
#     for c in range(20,60):
#         MANG[h][c]='5'

# tạo các điểm ngẫu nhiên theo quy luật hàm sin
# for c in range(199):
#     h=4*math.sin(0.2*c)-math.exp(0.02*c)+3*math.cos(0.08*c)
#     h=int(h+0.5)+60
#     MANG[h][c]='3'

# tạo hình cách hoa
# for t in range(1200):
#     t=t/100
#     h = (math.cos(2.99*t)-(math.sin(2.99*t))**2/math.sqrt(2))*math.sin(t)
#     c = (math.cos(2.99*t)-(math.sin(2.99*t))**2/math.sqrt(2))*math.cos(t)
#     h=int(30*h+0.5)+70
#     c=int(30*c+0.5)+140
#     print(h)
#     print(c)
#     MANG[h][c]='3'

# sau khi sử lí ảnh xong.  lưu lại vào file txt
b=open('map.txt','w',encoding='utf8')
for i in MANG:
    for j in i:
        b.write(j+' ')
    b.write('\n')   
b.close()
        
