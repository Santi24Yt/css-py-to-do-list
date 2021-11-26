# No javascript
For windows you need to add onto the regedit

**HKEY_CLASSES_ROOT \> pytest**

    (Default) | REG_SZ | URL:pytest protocol


**HKEY_CLASSES_ROOT \> pytest \> Shell \> Open \> Command**

    (Default) | REG_SZ | C:\Windows\py.exe -c "import os; import sys; from urllib.parse import unquote; args = sys argv[1:]; scrpath = unquote(args[0]).replace('pytest://', '')[:-1]; os.system('python '+scrpath)" "%L" %*

For linux idk.