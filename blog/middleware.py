# Function base middlewares
# def my_middleware(get_response):
#     print('One time Initialization')
#
#     def middleware(request):
#         print('This is before view')
#         response = get_response(request)
#         print('This is after view')
#         return response
#
#     return middleware


# Class base middleware
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('One time Initialization')

    def __call__(self, request):
        print('This is before view')
        response = self.get_response(request)
        print('This is after view')
        return response
