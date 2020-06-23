def wsgi_application(environ, start_response):
	data = environ['QUERY_STRING'].split('&');
	data = '\n'.join(data);
	data = bytes(data, encoding='utf-8');
	status = '200 OK';
	headers = [
		('Content-Type', 'text/plain'),
		('Content-Length', str(len(data)))
	];
	start_response(status, headers);
	return [data];
