import os
import natsort
#file = input('input')
file = './Chodi/Text'
os.system('rm ' + file + '/index.html')
with open(file + '/' + 'index.html', 'a+') as f:
    f.write("<head>\n         <link rel='stylesheet' href='https://collection.rishabh.gq/indexstyle.css'>\n</head>\n<p><span'><strong>Made By u/Rishabhmoodi</strong></span></p>")        
for o in natsort.natsorted(os.listdir(file)):
    print(o)
    o2 = o.replace('.html', '')
    with open(file + '/' + 'index.html', 'a+') as f:
        f.write("<a href=" + o +">" + o2 + "</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n")        
    