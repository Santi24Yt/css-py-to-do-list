import sys
import os

newPath = os.path.join(os.getcwd(), '\\'.join(__file__.split('\\')[:-1]))
os.chdir(newPath)

args = sys.argv[1:]

f = open('toDo.html', 'r')

i = args[0]
text = input('What needs to be done?\n_')

new = f.read().replace('<input type="checkbox" class="created-checkbox" id="created-checkbox-'+i+'"   />', '<input type="checkbox" class="created-checkbox" id="created-checkbox-'+i+'" checked  />')
new = new.replace('<label for="done-checkbox-'+i+'" class="mark-undone-checkbox-label"><a href="pytest://'+newPath+'\\undone.py '+i+'">Save</a></label>\n            <input required type="text" value="" class="todo-input" placeholder="What needs to be done?"/>', '<label for="done-checkbox-'+i+'" class="mark-undone-checkbox-label"><a href="pytest://'+newPath+'\\undone.py '+i+'">Save</a></label>\n            <input required type="text" value="'+text+'" class="todo-input" placeholder="What needs to be done?"/>')

n  = open('toDo.html', 'w')
n.write(new)
n.close()
f.close()