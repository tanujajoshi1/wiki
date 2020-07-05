from django.shortcuts import render
from django.http import HttpResponse
from . import util
from markdown2 import Markdown
import random
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def showMd(request,title):
	title=util.get_entry(title)
	return HttpResponse({title})

def showHTML(request,title):
	page=util.get_entry(title)
	if page is None:
		return render(request,"encyclopedia/error.html",{'message':"Requested page not found"})
	else:
		markdowner=Markdown()
		data=markdowner.convert(page)	
		data+='<button style="padding:10px 18px; border-radius:4px;color:blue;background-color:blue "><a style="color:white;font-size:17px;" href="edit/'+title+'">Edit Page</a></button>'
		return HttpResponse(data)


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
		return HttpResponse("Method not allowed")

def randomPage(request):
	list=util.list_entries()
	pages=random.choice(list)
	return HttpResponseRedirect(reverse("showHTML",args=[pages]))

def createPage(request):
	return render(request,"encyclopedia/create.html")

def savePage(request):
	if request.method=='POST':
		title=request.POST.get("title")
		textarea=request.POST.get("textarea")
		entries=util.list_entries()
		if title not in entries:
			util.save_entry(title,textarea)
			return HttpResponseRedirect(reverse("showHTML",args=[title]))
		else:
			return render(request,"encyclopedia/error.html",{'message':"A page with this title already exist"})


def editPage(request,title):
	data=util.get_entry(title)
	return render(request,"encyclopedia/edit.html",{'title':title,'data':data})

	
def edit(request):	
	if request.method=='POST':
		title=request.POST.get("title")
		data=request.POST.get("data")
		util.save_entry(title,data)
		return HttpResponseRedirect(reverse("showHTML",args=[title]))
	else:
		return HttpResponse("method is not allowed")













