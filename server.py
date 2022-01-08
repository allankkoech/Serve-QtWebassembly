import eventlet, os
from eventlet import wsgi


def dispatch(environ, start_response):

    """
        WEBSOCKETS
    """

    if environ['PATH_INFO'] == '/':
        start_response('200 OK', [('content-type', 'text/html')])
        return [open(os.path.join(os.path.dirname(__file__),
            'static/Portofolio.html')).read()]
   
    elif environ['PATH_INFO'] == '/qtloader.js':
        str_data = open(os.path.join(os.path.dirname(__file__),
            'static/qtloader.js')).read() 
        start_response('200 OK', [('content-type', 'application/javascript') ])

        return [str_data]

    elif environ['PATH_INFO'] == '/qtlogo.svg':
        img_data = open(os.path.join(os.path.dirname(__file__),
            'static/qtlogo.svg'), 'rb').read() 
        start_response('200 OK', [('content-type', 'image/svg+xml'),
                                ('content-length', str(len(img_data)))])

        return [img_data]

    elif environ['PATH_INFO'] == '/Portofolio.js':
        str_data = open(os.path.join(os.path.dirname(__file__),
            'static/Portofolio.js')).read() 
        start_response('200 OK', [('content-type', 'application/javascript')])
        return [str_data]

    elif environ['PATH_INFO'] == '/Portofolio.wasm':
        bin_data = open(os.path.join(os.path.dirname(__file__),
            'static/Portofolio.wasm'), 'rb').read() 
        start_response('200 OK', [('content-type', 'application/wasm')])
        return [bin_data]		

    elif environ['PATH_INFO'] == '/favicon.ico':
        img_data = open(os.path.join(os.path.dirname(__file__),
            'static/favicon.ico'), 'rb').read() 
        start_response('200 OK', [('content-type', 'image/x-icon'),
                                ('content-length', str(len(img_data)))])

        return [img_data]

    else:
        path_info = environ['PATH_INFO']
        print('PATH_INFO = {}'.format(path_info))
        return None
		

if __name__ == '__main__':
    listener = eventlet.listen(('127.0.0.1', 7000))
    print('\nVisit http://localhost:7000/ \n')
    wsgi.server(listener, dispatch)
