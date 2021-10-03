from django.shortcuts import render
from googletrans import Translator
# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        f = request.POST.get('from')
        t = request.POST.get('to')
        text = str(request.POST.get('content'))
        translator = Translator()
        trans = translator.translate(text, src= f , dest= t)
        context.update({'con' : trans.text, 't' : text, 'from' : f , 'to': t})
    return render(request,'trans/index.html',context)

 
# text1 = "Hello welcome to my website!"
 
# translator = Translator()

# trans1 = translator.translate(text1, src='en', dest='ja')

# print("English to Japanese: ", trans1.text)
