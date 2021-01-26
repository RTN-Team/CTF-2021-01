def rot(text, shift):
    result = ""
    for c in text:
        result += chr((ord(c) + shift) % 256)
    return result

for i in range(255):
    candidate = rot("MOIv/q.Z>\\`n/mZH+m,opm,ZO.ZN/gpo\iox", i)
    if candidate.startswith("RTN{"):
        print(candidate)
        break
        
