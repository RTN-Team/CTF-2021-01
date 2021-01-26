import os
import subprocess

while True:
    f = open("code.txt")
    pw = str(eval(f.readline()))
    f.close()
    
    subprocess.run(["unzip", "-P", pw, "-o", "file.zip"])

    print("Extracting file.zip with password", pw)

    if os.path.isfile("flag.txt"):
        break

print("Extraction completed.")