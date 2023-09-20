from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    
   #test - test results. i believe that outputting to a html page via redering requests cannot happen because of the way that i have made my project, in that the template system i am using requires a view each and the method of returning information to a page i am aware of also required its own view, meaning that i cannot both display the html template and return the information to the page as i am limited to 1 return per view 

    path('index/', views.index, name='index'),

    path('index_2/', views.index_2, name='index_2'),
#--------------------
    # /polls/homepage_page_html/
    path('homepage/',views.homepage, name='homepage'),

        # /polls/loginpage_page_html/
    path('loginpage/',views.loginpage, name='loginpage'),

       # /polls/loginpage_page_html/
    path('create_nu_page/',views.create_nu_page, name='create_nu_page'),

       # /polls/loginpage_page_html/
    path('treepage/',views.treepage, name='treepage'),

       # /polls/loginpage_page_html/
    path('extra_curricular_page/',views.extra_curricular_page, name='extra_curricular_page'),   

      # /polls/LinkTree/
    path('LinkTree/',views.LinkTree, name='LinkTree_page'),  

    #path('display_tree/',views.display_tree, name='display_tree_page'), 

    #path('tree_html/',views.tree_html, name='tree_html'), 

    #path('display_xml_as_tree/',views.display_xml_as_tree, name='display_xml_as_tree'), 
   #This path was to send the results of a new users input information to a web pag ( part way towards entering it into a sql model)
    #path('upload/', views.upload),

    #path('display_tree/',views.display_tree, name='display_tree_page'), 


]
