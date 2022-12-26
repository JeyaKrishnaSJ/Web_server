from http.server import HTTPServer, BaseHTTPRequestHandler
content="""
<html>
<head>
</head>
<body>
<h1>Django</h1>
</body>
</html>
"""
class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
         self.send_response(200)
         self.send_header('Content-type','text/html; charset=utf-8')
         self.end_headers()
         self.wfile.write(content.encode())


server_adress =('',80)
httpd =HTTPServer(server_adress, HelloHandler)
httpd.serve_forever()
print("My server is running")