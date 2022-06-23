import os
file = input('input')
os.system('rm ' + file + 'index.html')
with open('/workspace/arch/ind/' + 'index.html', 'a+') as f:
    f.write("<head>\n         <link rel='stylesheet' href='https://collection.rishabh.gq/indexstyle.css'>\n</head>\n<p><span'><strong>Made By u/Rishabhmoodi</strong></span></p>")        
for o in os.listdir('/workspace/arch'):
    print(o)
    o2 = o.replace('.html', '.txt')
    with open('/workspace/arch/ind/' + 'index.html', 'a+') as f:
        f.write("<a href=/" + o +">" + o2 + "</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n")        
    