import os
file = '../../'
os.system('rm ' + file + 'index2.html')
with open(file + 'index2.html', 'a+') as f:
    f.write("        <style>\n            li {\n  color: white;\n  font-family: sans-serif;\n  font-size:3vh;\n}\n        </style>\n<p><span style='font-size: 14pt; color: black;'><strong>Made By u/Rishabhmoodi</strong></span></p>")        
for o in os.listdir(file):
    print(o)
    with open(file + 'index2.html', 'a+') as f:
        f.write("<li><a href='" + o + "'><span style='font-family: 'andale mono', monospace;'><strong>" + o + "</strong></span> </a></li>")        
    