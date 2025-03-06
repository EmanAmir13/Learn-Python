# Function base middlewares

def my_middleware(get_response):
    print('One time Initialization')

    def middleware(request):
        print('This is before view')
        response = get_response(request)
        print('This is after view')
        return response

    return middleware
