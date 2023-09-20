
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
#from mysite.polls.forms import UploadForm
from polls.models import ModuleLinking
from django.core import serializers
import xml.dom.minidom

def index(request):
   
    test_index = "hello"
    context = {'test_index': test_index}
   # Link_Module_codes = [ModuleLinking.Link_Module_code for ModuleLinking in MYMODEL]
    #return render(request, 'polls/index.html', {'Link_Module_codes:': Link_Module_codes})

#unsure why it isnt working will try and create two views that outpout to the same web page?
   # return render(request, 'polls/index.html' , {'MYMODEL': MYMODEL} )
    return render(request, 'polls/index.html' , context )

def index_2(request):
    MYMODEL = ModuleLinking.objects.all()
    return render(request, 'polls/index.html' , {'MYMODEL': MYMODEL} )
#TESTING -----------------------------------------------------------

def homepage(request): #try adding if/endif bit in tutorial
    call_text_homepage = "hello"
    context = {'call_text_homepage': call_text_homepage}
    return render(request, 'polls/homepage.html', context)

def loginpage(request): 
    call_text_loginpage = "hello"
    context = {'call_text_loginpage': call_text_loginpage}
    return render(request, 'polls/loginpage.html', context)

def create_nu_page(request): 
    call_text_newsserpage = "hello"
    context = {'call_text_newsserpage': call_text_newsserpage}
    return render(request, 'polls/create_nu_page.html', context)

def treepage(request): 
    call_text_treepage = "hello"
    context = {'call_text_treepage': call_text_treepage}
    return render(request, 'polls/treepage.html', context)

def extra_curricular_page(request): 
    call_text_ECpage = "hello"
    context = {'call_text_ECpage': call_text_ECpage}
    return render(request, 'polls/extra_curricular_page.html', context)

def LinkTree(request):
    #XMLSerializer = serializers.get_serializer("xml")
    #xml_serializer = XMLSerializer()
    queryset = ModuleLinking.objects.all()
    serialzed_data = serializers.serialize('xml', queryset)
    #return HttpResponse(queryset,content_type="application/xml")
    with open("file.xml", "w") as out:
       #queryset(ModuleLinking.objects.all(), stream=out)
        out.write(serialzed_data)
    return HttpResponse("file.xml", "w")

#-----------------------------------------------



""" UNCOMMENT HERE
#This class generates my xml document called file.xml
def LinkTree(request):
    #XMLSerializer = serializers.get_serializer("xml")
    #xml_serializer = XMLSerializer()
    queryset = ModuleLinking.objects.all()
    serialized_data = serializers.serialize('xml', queryset)
    #return HttpResponse(serialized_data, content_type='application/xml') # this line outputs my xml to my linktree page
    #return HttpResponse(queryset,content_type="application/xml")
    with open("file.xml", "w") as out:
        queryset(ModuleLinking.objects.all(), stream=out)
        out.write(serialized_data)
    return HttpResponse("file.xml", "w") # this is a stand in feature that will post "file.xml" to the page instead of truley posting the file
    

#-----------------------------------------------

def tree_html(request): #this definition should link to the URL tree_html and output the HTML template tree_html.html
    tree_html = "hello"
    context = {'tree_html': tree_html}
    return render(request, 'polls/tree_html.html', context)

import xml.dom.minidom # mini dom moduel is imported

#this view takes an XML node and returns it as a string on the web page
def display_tree(node, level=0): # a node is passed to the function and an indentation variable is passed to it

    indentation = "    " * 4 * level # this indentation level will allow the html string on the page to be seperated on the page by the "    " string multiplied by the level value

    html = f"<p>{indentation}{node.nodeName}</p>" # this line passed

    if node.firstChild and node.firstChild.nodeType == node.firstChild.nodeType: # this checks if the node values match and then assignes the value of that node to "nodetext"
        nodetext = node.firstChild.nodeValue

    if nodetext: # opens an if loop is node text has a variable
        html += f"<p>{indentation}    {nodetext}</p>" # this designs the outputted html that will be displayed and allows the string to have variable inputted to it

    for child in node.childNodes: # this shoudl open the child nodes for nodetext
        if child.nodeType == child.ELEMENT: # check to see if node is element node type
            html += display_tree(child, level + 1) # sets child to html however with an increase in the indent level 
    return html


def display_xml_as_tree(xml_string): # call in xml string
    dom = xml.dom.minidom.parseString(xml_string) # this line parses the value of xml string to dom of which will represent the xml in the DOM format
    root_element = dom.documentElement # the root element of the xml document is extracted and assigned to root_element
    return display_tree(root_element)

with open("file.xml", "r") as file:
    xml_string = file.read()
    tree_html = display_xml_as_tree(xml_string)

with open("tree_html.html", "r") as file:
    tree_html = file.read()

tree_html = tree_html.replace("{{tree}}", tree_html)
print(tree_html)
"""
#this segment outputs values from the xml doc to the terminal using indentation
def display_tree(node, nodelevel=0):
    indentation = "  " *nodelevel
    print(f"{indentation}{node.firstChild.nodeValue}") #This line
    for child in node.childNodes:
        if child.nodeType ==child.ELEMENT_NODE:
            display_tree(child, nodelevel+1)

# Load the XML document
doc =xml.dom.minidom.parse("file.xml")

# Display the tree structure starting from the root element
root =doc.documentElement
display_tree(root)


#def display_xml_as_tree(xml_string):
    # Create an instance of the XML DOM
   # dom = xml.dom.minidom.parseString("file.xml")
    #print(dom.nodeName)

#---------------------------
# This code was working towards allowing the user to input information when creating a new user

#def upload(request):
 #  form = UploadForm(request.POST, request.POST,request.POST,request.POST,request.POST,request.POST,request.POST,request.POST,request.POST,request.POST,request.POST,request.POST,)
  # return render(request, 'polls/upload.html', {'form' : form})

