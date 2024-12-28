from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<html>
    <head>
        <h1><b><center>LAPTOP CONFIGURATION</center></b></h1>
    </head>
    <BODY>
        <table border= "3" bgcolor="pink" cellpadding="20" cellspacing="10" align="center">
            <tr>
                <th>System configuration</th>
                <th> Description</th>
            </tr>
            <tr>
                <th>Processor</th>
                <th>i5</th>
            </tr>
            <tr>
                <th>Primary Memory</th>
                <th>Ram 16 GB</th>
            </tr>
            <tr>
                <th>Secondary Memory</th>
                <th>512 GB</th>
            </tr>
            <tr>
                <th>0.S</th>
                <th>Windows 11</th>
            </tr>
            <tr>
                <th>Graphic</th>
                <th>nvidia</th>
            </tr>
            </table>

    </BODY>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()