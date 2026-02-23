import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Find the handler of npc_dialog_open event
webgl = open('assets/webgl-C4v7tvuW.js', encoding='utf-8', errors='ignore').read()
App3D = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()

# Search in webgl
idx = webgl.find('npc_dialog_open')
if idx != -1:
    print("webgl npc_dialog_open handler:")
    print(webgl[idx-200:idx+600])
else:
    print("Not in webgl")
    
# Also search in runtime
runtime = open('assets/runtime-C2kxzoFi.js', encoding='utf-8', errors='ignore').read()
idx2 = runtime.find('npc_dialog_open')
if idx2 != -1:
    print("\nruntime npc_dialog_open handler:")
    print(runtime[idx2:idx2+400])

# Find the quest checklist text rendering  
idx3 = App3D.find('checklist-text')
print(f"\nchecklist-text at {idx3}")
print(App3D[idx3-100:idx3+400])
