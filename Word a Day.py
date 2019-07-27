import urllib.request
import codecs

url = "https://feeds.feedblitz.com/mandarin-chinese-word-of-the-day&x=1"

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
fullSource = response.read()
fullSource = fullSource.decode("utf-8")

# Get the Pinyin

startPos = fullSource.index("Pinyin")
tempString = fullSource[startPos:]
startPos = tempString.index(">")+1
tempString = tempString[startPos:]
startPos = tempString.index(">")+1
endPos = tempString.index("</td>")

pinyinFinal = tempString[startPos:endPos]

# Get the Definition

startPos = fullSource.index("<title>")
tempString = fullSource[startPos+2:]
startPos = tempString.index("<title>")
tempString = tempString[startPos:]
startPos = tempString.index("A[")+5
endPos = tempString.index("]]")

defineFinal = tempString[startPos:endPos]

finString = pinyinFinal.capitalize() + ": " + defineFinal.capitalize()

f=codecs.open("wotd.html","w+","utf-8")
f.write(finString)
f.close()
