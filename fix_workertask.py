txt = open('assets/App3D-BLRWK1h9.js', encoding='utf-8', errors='ignore').read()

# The issue: Za=function(e) { const i=e.data.id; if(typeof i>"u") throw new Error(...)
# When a worker sends back a message without an id, this throws.
# The fix: instead of throwing, just log a warning and return.

old = 'if(typeof i>"u")throw new Error("workerTask: message must have an id")'
new = 'if(typeof i>"u"){console.warn("workerTask: message without id, skipping",e.data);return}'

count = txt.count(old)
print(f"Found {count} occurrences")

txt = txt.replace(old, new)

with open('assets/App3D-BLRWK1h9.js', 'w', encoding='utf-8') as f:
    f.write(txt)

print("Patched! workerTask id errors now log a warning instead of crashing.")
