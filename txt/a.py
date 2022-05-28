import os
for a in os.listdir('./'):
    a1 = a.replace('.txt', '.html')
    os.system("mv " + a + ' ' + a1)