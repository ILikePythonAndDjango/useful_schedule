import json

from django.http import HttpResponse

'''
This module contains classes for handling http/https requests which called AJAX API!
'''

class HttpResponseAjax(HttpResponse):

    '''
    This class works with AJAX requests!
    '''

    def __init__(self, status='ok', **kwargs):
        kwargs['status'] = status
        super(HttpResponseAjax, self).__init__(
            content=json.dumps(kwargs),
            content_type='application/json'
        )

class HttpResponseAjaxError(HttpResponseAjax):

    '''
    When is error in AJAX request this class get response!
    '''

    def __init__(self, code, message):
        super(HttpResponseAjaxError, self).__init__(
            status='error', code=code, message=message
        )