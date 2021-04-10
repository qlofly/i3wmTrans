# Translator for i3wm
Python script to translate text using highlight and keyboard shortcut

#Installing a dependency:
  
  pip install pyperclip
  -Install a package "translate-shell" for your distribution
  
#You need to add a line to the i3wm config, changing it to fit your data:

  bindsym $mod+x exec --no-startup-id "/usr/bin/python /path/to/i3wmTrans.py"

-Configure 'translate-shell' before use. For more information, enter 'trans --help' in a terminal.
# Usage: 
-Copy text to clipboard and press your key combination. You can see the translated text in the notification
