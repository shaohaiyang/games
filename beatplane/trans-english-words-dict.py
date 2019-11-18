#!/opt/python374/bin/python3.7
dic = dict()
file = "little-school-english-words.txt"
with open(file,'r') as f:
  for line in f:
    if not line:
      break
    elif line.strip() == "":
      pass
    else:
      line = line.strip('\n')
      k = str(len(line))
      dic.setdefault(k, []).append(line)

for k,v in dic.items():
  print("%s:%s," % (k,v))  
