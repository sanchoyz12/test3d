txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()

# Find where "workerTask: message must have an id" comes from
idx = txt.find('message must have an id')
print(f"workerTask error at {idx}")
print(txt[idx-300:idx+200])
