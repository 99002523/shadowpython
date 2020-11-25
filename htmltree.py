from htmldom import htmldom
dom = htmldom.HtmlDom()
#or
dom = htmldom.HtmlDom( "http://www.example.com" )

dom = dom.createDom("<html></html>")
#or, if you have provided the url then just createDom() call will suffice
dom = dom.createDom()
