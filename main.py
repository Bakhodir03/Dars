# #1-misol
# a = float(input("a sonni kiritin:a="))
# b = float(input("b sonni kiriting:b="))
#
# while a>=b:
#     a-=b
# print(a)
#2-misol
# a = float(input("a sonni kiritin:a="))
# b = float(input("b sonni kiriting:b="))
# soni=0
# while a>b:
#     a-=b
#     soni+=1
# print(soni)
#3-misol
# N = float(input("N sonni kiritin:a="))
# K = float(input("K sonni kiriting:b="))
#
# while N>=K:
#     N-=K
# print(N)
#4-misol
# n = float(input("N sonni kiritin:a="))
# while n>0:
#     n-=3
# if n==0:
#     print( "3 ning darajasi")
#
# else:
#      print("emas")
#5-misol
# n = int(input("N sonini kiriting: "))
#
# m = 1
# daraja = 0
#
# while m < n:
#     m *= 2
#     daraja += 1
#
# if m == n:
#     print(daraja)
# else:
#     print("Bu son 2 ning darajasi emas.")
import math
from binascii import a2b_qp
from bisect import insort_right
from time import perf_counter
from xml.etree.ElementPath import prepare_parent
from xxsubtype import bench

#6-misol
# n = int(input("N sonini kiriting: "))
# naija=1
# while n>0:
#     naija*=n
#     n-=2
# print(naija)
#7-misol
# n = int(input("n sonini kiriting:"))
# a=0
# while n>0:
#     a+=1
#
#     if a**2>n:
#         break
# print(a)
#8-misol
# n = int(input("n sonni kiriting:n="))
# a=0
# while n>0:
#    a+=1
#    if a**2>n:
#        break
# print(a-1)
#9-misol
# n = int(input("n sonni kiriting:n="))
# k=1
# while n>0:
#     k+=1
#     if 3**k>n:
#         break
# print(k)
#10-misol
# n = int(input("n sonni kiriting:n="))
# k=1
# while n>0:
#     k+=1
#     if 3**k>n:
#         break
# print(k-1)
#11-misol
# n = int(input("n sonni kiriting:n="))
# k=0
# y=0
# while n>0:
#     k+=1
#     y+=k
#     if y>=n:
#         break
#
# print(y)
#12-misol
# n = int(input("n sonni kiriting:n="))
# k=0
# y=0
# while n>0:
#     k+=1
#     y+=k
#     if y>=n:
#         break
# print(y-k)
#13-misol
# n = float(input("n sonni kiriting:n="))
# b=0
# k=0
# while n>0:
#     b+=1
#     k+=1/b
#     if k>=n:
#         break
# print(k)
#14-misol
# n = float(input("n sonni kiriting:n="))
# b=0
# k=0
# while n>0:
#     b+=1
#     k+=1/b
#     if k>=n:
#         break
# print(k-1)
#15_misol

# boshlabgich_som = float(input("Birinchi qo'ygan summani kiriting: "))
# p = float(input("Foizni kiriting (masalan, 10): "))
# oxirgi_summa = boshlabgich_som * 2
#
# oylar = 0
#
# while boshlabgich_som< oxirgi_summa:
#     foiz = (boshlabgich_som * p) / 100
#     boshlabgich_som += foiz
#     oylar += 1
#
# print(f"{oylar} oyda kiritilgan summa 2 baravarga oshadi.")
# print(oxirgi_summa)
#16-misol
# p = int(input("qo\'shilgan foizni kiriting:p="))
# birinchi_kun = 100
# oxirgi_kuni=200
# kun=0
# while birinchi_kun<oxirgi_kuni:
#     foiz = (birinchi_kun*p)/100
#     birinchi_kun+= foiz
#     kun+=1
# print(kun)
#17-misol
# n = int(input("n sonni kirirting:n="))
# m = int(input("m sonni kirinting:m="))
# b=0
# while n>m:
#      a = n-m
#      b+=1
#      n=a
#      if a<m:
#          break
# print(b)
# print(a)
#18-misol
# n = int(input("Butun son kiriting (n ≥ 0): "))
# teskarilash = 0
#
# while n > 0:
#     oxirgi_son = n % 10
#     teskarilash= teskarilash * 10 +oxirgi_son
#     n = n // 10
# print("Sonning teskari tartibi:", teskarilash)
#19-misol

# n = int(input("Butun son kiriting (n ≥ 0): "))
# teskarilash = 0
# yigindi=0
# while n > 0:
#     oxirgi_son = n % 10
#     teskarilash= teskarilash * 10 +oxirgi_son
#     n = n // 10
#     yigindi +=oxirgi_son
# print("Sonning teskari tartibi:", teskarilash)
# print(yigindi)
#20-misol
# n = int(input("Butun son kiriting (n ≥ 0): "))
# found = False
# while n > 0:
#     oxirgi_son = n % 10
#
#     if oxirgi_son==2:
#         found = True
#         break
# if found:
#     print( "2 raqami bor")
# else:
#     print("2 raqami yoq")
#21-misol
# n = int(input("Butun son kiriting (n ≥ 0): "))
# found = False
#
# while n > 0:
#     oxirgi_son = n % 10
#
#     if oxirgi_son /2 != 0:  # Toq raqamni tekshirish
#         found = True
#         break
# if found:
#     print("Toq raqam bor")
# else:
#     print("Toq raqam yo'q")
#22- misol
# n = int(input("Butun son kiriting : "))
# if n>1:
#     a=2
#     son=True
#     while a<n:
#         if n%a==0:
#             son=False
#             break
#             a+=1
#     if son:
#         print(f"{n} tub son")
#     else:
#         print(f"{n } tub son emas:")
# else:
#     print("faqan 1 dan kattta son kiriting:")
#23-misol
# a= int(input("a sonni kirirtibg:"))
# b=int(input("b sonnin kiriting:"))
# while a!=b:
#     if a>b:
#         a=a-b
#     else:
#         b=b-a
# print(a)
#24-misol
# n =  int(input("n sonini kiriting:"))
# a=1
# b=1
#
# foun =False
# while a<=n:
#     if a==n:
#         foun =True
#         break
#     d = a + b
#     a=b
#     b=d
#
# if foun:
#     print("kiritilgan son fibanachi soni:")
# else:
#     print("fibanachi soni emas:")
#25-misol
# n =  int(input("n sonini kiriting:"))
# a=1
# b=1
#
# foun =False
# while b<=n:
#     d = a + b
#     a=b
#     b=d
# print(f"{n}\tsonidan katta bo'gan son {b}")
#26-miosl
# n =  int(input("n sonini kiriting:"))
# a=1
# b=1
#
# foun =False
# while b<=n:
#
#     d = a + b
#     a=b
#     b=d
# print(f"birinchi fibanichi soni {a}")
# print(f"{n}\tsonidan katta bo'gan son {b}")

#27-misol
# n =  int(input("n sonini kiriting:"))
# a=0
# b=1
# soni=0
# foun =False
# while b<=n:
#
#     d = a + b
#     a=b
#     b=d
#     soni+=1
# # print(f"birinchi fibanichi soni {a}")
# # print(f"{n}\tsonidan katta bo'gan son {b}")
# print(soni)

#28-misol
# e = float(input("e sonni kiriting:"))
# a1=2
# k=1
# while True:
#     k+=1
#     a2=2+1/a1
#     a1=k-1
#     print(f"k={k}\t a1={a1} a2={a2}")
#     if math.fabs(a1-a2)<e:
#         break
#         a1 = a2
# print("k=",k)
#29-misol

# e = float(input("e sonni kiriting: "))
# a1 = 1
# a2 = 2
# k = 1
#
# while True:
#     k += 1
#     d = (a1 + 2 * a2) / 3
#     a1 = a2
#     a2 = d
#     print(f"k={k}\t a1={a1} a2={a2}")
#
#     if math.fabs(a1 - a2) < e:
#         break
#
# print("k =", k)
#30-misol
# a = int(input("a tomonni kiriting: a = "))
# b = int(input("b tomonini kiriting: b = "))
# c = int(input("Kvadrat tomonini kiriting: c = "))
# if a >= c and b >= c and c > 0:
#     a_soni = 0
#     temp_a = a
#     while temp_a >= c:
#         temp_a -= c
#         a_soni += 1
#
#     b_soni = 0
#     temp_b = b
#     while temp_b >= c:
#         temp_b -= c
#         b_soni += 1
#
#     kvadrat_son = 0
#     u_soni = a_soni
#     while u_soni > 0:
#         kvadrat_son += b_soni
#         u_soni -= 1
#
#     print(f"Jami {kvadrat_son} ta kvadrat joylashishi mumkin.")
# else:
#     print("Tomonlarni to'g'ri kiriting!")














