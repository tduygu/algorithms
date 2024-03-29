# def myFunc(n):
#     res = 1
#     for i in range(n,n+2,1):
#         print(res)
#         yield res
#         res*=2
#
# y = [x for x in myFunc(3)]
# print(y)

##################################3#######33
# a = 5
# print(a)
# for i in range(5,7):
#     a*=2
#     print(a)

# Ya return list olur, liste yoksa her bir elemanı üzerinde işlem yapılabilecek gibi fonksiyonun sıra sıra elemanı dışarı vermesi (püskürtmesi)
# gerekir, yani iterable olması gerekir. Bunu da yield ile sağlıyoruz.

# yield res demek for döngüsü içinde üretilen her bir eleman üzerinde işlem yapabilirsin demek, returnü olmasa bile bu fonksiyon bir dizi eleman
# çıktısı veriyormuş gibi davranır.

def myFunc(n):
    res = 1
    #lst = []
    for i in range(n):
        print(res)
        #yield res
        res *= 2
        yield res # yield res'in burada olması ile yukarıda olması değişiklik gösterir. dışarıya verdiği res değeri farklıdır.
        #lst.append(res)
    #return lst

myFunc(3)

y = [x for x in myFunc(3)]
print(y)

