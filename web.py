import feedparser
import xml.etree.ElementTree as ET


file = open("item1.xml", "w")
data = ET.Element('data')
items = ET.SubElement(data, 'items')
feed = []

f = feedparser.parse("https://mangadex.org/rss/YdynXZpTkB2fqtg6S5NR9xMUrPzGCVQw/manga_id/31477")

entries = f.entries

for d in entries:
	split = d.description.split()
	c = 0
	for t in split:
		if t == 'Language:':
			l = c + 1
		else:
			c += 1
	if split[l] == "English":
		feed.append(d.title + " " + split[l] + " Release: " + str(d.published_parsed[2]) + "/" + str(d.published_parsed[1]) + "/" + str(d.published_parsed[0]) + " " + str(d.published_parsed[3]) + ":" + str(d.published_parsed[4]))
		item = ET.SubElement(items, 'item')
		title = ET.SubElement(item, 'title')
		lang = ET.SubElement(item, 'lang')
		date = ET.SubElement(item, 'date')
		title.text = d.title
		lang.text = split[l]
		date.text = str(d.published_parsed[2]) + "/" + str(d.published_parsed[1]) + "/" + str(d.published_parsed[0]) + " " + str(d.published_parsed[3]) + ":" + str(d.published_parsed[4])


mydata = ET.tostring(data, method="xml")
splitdata = mydata.split()
print(splitdata)
file.write(str(mydata))

for f in feed:
	print(f)