
strs = ["flower", "flow", "flight"]
if not strs:
    c_pref = ""
else:
    c_pref = strs[0]
    for word in strs[1:]:
        while not word.startswith(c_pref):
            c_pref = c_pref[:-1]
            if not c_pref:
                break
print(c_pref)