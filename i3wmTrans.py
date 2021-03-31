import pyperclip
import subprocess
import os

x = pyperclip.paste()

w = ('"%s"' % x)
print(w)
work = os.popen("trans -b -e bing " + str(w)).read()
work = ('"%s"' % work)

os.system('notify-send Перевод: ' + str(work))

