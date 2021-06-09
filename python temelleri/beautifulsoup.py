html_doc ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First Web page</title>
</head>
<body>
    
</body>
    <h1>
        Python Kursu (Temel Baslik)
    </h1>
    <div class="grup1">
        <h2> 
            Programlama 
        </h2>
        <ul>
            <li>Menu  1</li>
            <li>Menu  2</li>
            <li>Menu  3</li>
        </ul>
    </div>

    <img src="fred.jpg" alt="">
    <div class="grup2">
        <h2> 
            Moduller
        </h2>
        <ul>
            <li>Menu  1</li>
            <li>Menu  2</li>
            <li>Menu  3</li>
     </ul>
    </div>
</html>
"""
"""
from bs4 import BeautifulSoup
sup =BeautifulSoup(html_doc,"html.parser")
result =sup.prettify() #duzenleme yapiyo
result =sup.title
result =sup.h1
result =sup.find_all("div")[1]
result =sup.findChildren() #btutn alt elemablar
print(result)
"""
"""
import requests
from bs4 import BeautifulSoup
url ="https://www.imdb.com/chart/top/"
respo=requests.get(url)
print(respo)
"""
import imp 
a =imp.find_module("re")
print(a)