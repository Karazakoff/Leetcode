from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for attr in attrs:
                print("->", attr[0], ">", attr[1])
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        if attrs:
            for attr in attrs:
                print("->", attr[0], ">", attr[1])

# instantiate the parser and fed it some HTML

parser = MyHTMLParser()
number = int(input())
result = ""
for _ in range(number):
    result += input()
parser.feed(result)
