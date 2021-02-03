import urllib.request
f=urllib.request.urlopen("http://www.example.com")
for line in f:
    print(line.decode())
