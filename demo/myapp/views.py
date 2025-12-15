from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .utils import load_documents
from .utils import split_documents

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items })

def load_pdfs(request):
    documents = load_documents()
    chunks = split_documents(documents)
    context = {
        "documents": documents,
        "chunks": chunks,
        "num_documents": len(documents),
        "num_chunks": len(chunks),
    }
    return render(request, "load_pdfs.html", context)
    #return HttpResponse("Loaded " + str(len(documents)) + " documents.")
