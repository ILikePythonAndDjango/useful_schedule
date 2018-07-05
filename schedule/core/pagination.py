from django.core.paginator import Paginator, EmptyPage

def _validate_data_for_pagination(request):

    '''
    Checks and return Get params: limit, page.
    '''

    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10

    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    return limit, page

def paginate_HTML(request, qs):

    '''
    paginate(request, qs) => tuple(paginator, page)
    This function paginates with all rules:
    1. Checks the validity of limit and page
    2. If function get uncorrect parameters then it raises exception Http404
    3. Function does within limit <= 100
    '''

    limit, page =_validate_data_for_pagination(request)

    paginator = Paginator(qs, limit)

    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page

def paginate_JSON(request, qs):

    """
    Does as paginate_HTML but returns only JSON instead HTML and Paginator's object
    """
    
    limit, page = _validate_data_for_pagination(request)

    begin = limit * page

    return qs.objects.all()[begin:begin+limit:]