from django.shortcuts import render
from django.http import HttpResponse
from . import util
from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def showMd(request,title):
	title=util.get_entry(title)
	return HttpResponse({title})

def showHTML(request,title):
	page=util.get_entry(title)
	markdowner=Markdown()
	return HttpResponse(markdowner.convert(page))


def search(request):
	if request.method=='POST':		
		name=request.POST.get("search")
		entries=util.list_entries()
		page=util.get_entry(name)
		markdowner=Markdown()
		if name in entries:
			return HttpResponse(markdowner.convert(page))
	    
		res=[i for i in entries if name in i]
		if res is not None:	
			return render(request, "encyclopedia/search.html",{"entries":res})
		
	else:
		return HttpResponse("Method not found")
