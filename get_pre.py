from bs4 import BeautifulSoup
import os


directory = '/var/www/html/workbook/'

data="<html><body>"
for root, dirs, files in os.walk(directory):
    for filename in files:
        if "html" in filename:
            #print(os.path.join(root, filename))
            with open(os.path.join(root, filename),"r") as f:
                html=f.read()

            soup = BeautifulSoup(html, "html.parser")
            for tag in soup.find_all():
                if(tag.name == "pre"):
                    data+="<pre>"+tag.get_text()+"</pre>"

data+="</body></html>"
with open("output.html","w") as w:
    w.write(data)

