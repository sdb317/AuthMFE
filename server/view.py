###########################################################
## File        : View.py
## Description : 

import re
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from . import settings

# Class Dependencies

import django.views.generic

class View(django.views.generic.TemplateView):

# Class Attributes

    context={k:v for (k,v) in settings.__dict__.items() if re.search('__.*__', k) == None and type(v) is str}

# Constructor

    def __init__(self):

# Instance Attributes


# Class Initialisation

        super(View, self).__init__()
        return

# Operations

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self,*args,**kwargs):
        return super(View, self).dispatch(*args, **kwargs)

    def get_context_data(self,**kwargs):
        context = super(View, self).get_context_data(**kwargs) # Call base implementation to get a context then merge in str values from settings.py
        context.update(View.context)
        return context

