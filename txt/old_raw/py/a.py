import os
for a in os.listdir('./'):
    print("<li><a href='" + a + "'><span style='font-family: 'andale mono', monospace;'><strong>" + a + "</strong></span> </a></li>")