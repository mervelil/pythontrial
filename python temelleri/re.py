
"""
import re
#res =dir(re)
str ="aya benzer e dogal"
#res =re.findall("aya",str)
result = re.split(" ",str)
result =re.sub(" ","-",str)
result =re.search("aya",str)
result =re.span()
result=re.findall("[a-z]",str)
result=re.findall("[1-9]",str)
result=re.findall("[^abc]",str) #sunlar haric . her bir karakteri belirtir
result =re.findall("...",str)
result =re.findall("a..",str) #true
result=re.findall("^a",str) #belirtilen harfle baslıyor mu
result =re.findall("l$",str) #somda l harfi var mı boolean degil list olarak dondurur
result=re.findall("sa*t",str)#* harften bir ya da fazla mı onu kontrol eder
#soru isareti ise  0 ya da 1 tane olmasınını kontol eder
result=re.findall("[0-9]{2}",str) #2 basamaklıları kontrol eder
result=re.findall("a{2}",str)

(a|b|x)xz#abc karakterilernden arkasina xz gelmeli
\Athe  the stringin basinda mi
\zthe the str sonunda mı
resuly =re.findall("\Aaya",str)
print(res)
"""