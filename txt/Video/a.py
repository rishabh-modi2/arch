import os
file = './'
os.system('rm ' + file + 'index2.html')
with open(file + 'index2.html', 'a+') as f:
    f.write("        <head>\n         <link rel='stylesheet' href='https://collection.rishabh.ml/videostyle.css'>\n<p><span'><strong>Made By u/Rishabhmoodi</strong></span></p>")        
for o in os.listdir(file):
    print(o)
    with open(file + 'index2.html', 'a+') as f:
        f.write("<li><a href='" + o + "'><span style='font-family: 'andale mono', monospace;'><strong>" + o + "</strong></span> </a></li>")        
    