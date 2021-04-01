###########################################################
## File        : UserViewSet.py
## Description : 

import logging
logging.basicConfig(level=logging.DEBUG)
from django.contrib.auth import authenticate, login, logout
from rest_framework import response, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, action

# Class Dependencies

import rest_framework.viewsets


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # Effectively disable csrf check
    
class UserViewSet(rest_framework.viewsets.ViewSet):

# Class Attributes

    authentication_classes=(CsrfExemptSessionAuthentication,)

# Constructor

    def __init__(self,**kwargs):

# Instance Attributes


# Class Initialisation

        super(UserViewSet, self).__init__(**kwargs)
        return

# Operations

    def get_permissions(self):
        #logging.info('UserViewSet.get_permissions')
        #if self.action in ('create',): # 'POST'
        #    self.permission_classes = [AllowAny, ] # Anyone can try to authenticate
        #else:
        #    self.permission_classes = [IsAuthenticated, ]
        self.permission_classes = [AllowAny, ] # Anyone can try to authenticate
        return super(self.__class__, self).get_permissions()

    @action(methods=['post'], detail=False, url_path='login', url_name='post-login')
    def login(self,request):
        logging.info('UserViewSet.login')
        try:
            user = authenticate(request, username=request.data['username'], password=request.data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    details = {
                        'username': user.username,
                        'authenticated': user.is_authenticated,
                        'firstName': user.first_name,
                        'lastName': user.last_name,
                        'email': user.email,
                    }
                    return response.Response({'success': {'user': details}}, status=status.HTTP_200_OK, content_type='application/json')
                else:
                    return response.Response({'failure': 'UserViewSet.create - Disabled account'}, status=status.HTTP_401_UNAUTHORIZED, content_type='application/json')
            else:
                return response.Response({'failure': 'UserViewSet.create - Invalid login'}, status=status.HTTP_401_UNAUTHORIZED, content_type='application/json')
        except Exception as e:
            return response.Response({'failure': 'UserViewSet.create - %s'%e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type='application/json')
        return

    @action(methods=['post'], detail=False, url_path='logout', url_name='post-logout')
    def logout(self,request):
        logging.info('UserViewSet.logout')
        try:
            logout(request)
            return response.Response({'success': {'user': {}}}, status=status.HTTP_200_OK, content_type='application/json')
        except Exception as e:
            return response.Response({'failure': 'UserViewSet.destroy - %s'%e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type='application/json')
        return

