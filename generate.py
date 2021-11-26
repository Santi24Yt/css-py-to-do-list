import sys
import os

newPath = os.path.join(os.getcwd(), '\\'.join(__file__.split('\\')[:-1]))
os.chdir(newPath)

args = sys.argv[1:]

maxItems = int(args[0]) if len(args) > 0 else 50

def generateItems(i):
    if i > maxItems:
        return ''

    return ('''
        <div id="todo-'''+ str(i) +'''" class="todo">

            <input type="checkbox" class="created-checkbox" id="created-checkbox-'''+ str(i) +'''" '''+ ('checked' if i == 0 else ' ') +''' /> <!--Check for created-->

            <input type="checkbox" class="deleted-checkbox" id="deleted-checkbox-'''+ str(i) +'''" />

            <input type="checkbox" class="done-checkbox" id="done-checkbox-'''+ str(i) +'''" '''+ ('checked' if i == 0 else ' ') +''' /> <!--Check for done-->
            <label for="done-checkbox-'''+ str(i) +'''" class="mark-done-checkbox-label"><a href="pytest://'''+newPath+'''\\done.py '''+ str(i) +'''">Save</a></label>
            <label for="done-checkbox-'''+ str(i) +'''" class="mark-undone-checkbox-label"><a href="pytest://'''+newPath+'''\\undone.py '''+ str(i) +'''">Save</a></label>
            <input required type="text" value="" class="todo-input" placeholder="What needs to be done?"/> <!--Change value="" for the todo-->
            <label for="created-checkbox-'''+ str(i) +'''" class="created-checkbox-label"><a href="pytest://'''+newPath+'''\\save.py '''+ str(i) +'''" style="padding: 15px">Add</a></label>
            <div class="items-left-counter-helper"></div>
            '''+ generateItems(i+1) +'''
        </div>
    ''')

f = open('toDo.html', 'w')

html = '''<html>
  <head>
    <link href="./style.css" rel="stylesheet">
    <link href="./toDo.css" rel="stylesheet">
  </head>
  <body>
    <input type="checkbox" id="toggle-box">
    <label for="toggle-box">Toggle!</label>
    <div id="content">
      Hello world!
    </div>
    <div>
        '''+ generateItems(0) +'''
    </div>
  </body>
</html>'''

f.write(html)
f.close()
