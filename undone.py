import sys
import os

newPath = os.path.join(os.getcwd(), '\\'.join(__file__.split('\\')[:-1]))
os.chdir(newPath)
args = sys.argv[1:]

f = open('toDo.html', 'r')

i = args[0]

new = f.read().replace('<input type="checkbox" class="done-checkbox" id="done-checkbox-'+i+'" checked  />', '<input type="checkbox" class="done-checkbox" id="done-checkbox-'+i+'"   />')

n  = open('toDo.html', 'w')
n.write(new)
n.close()
f.close()