#!F:\python\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi, cgitb
form = cgi.FieldStorage() 

# Get data from fields
response = form.getvalue('userid')
print("<html>")
print("<head>")
print("<title>my form page</title>");
print("</head>");
print("<body>")
print("<p>response</p>");

print("</body>");
print("</html>");


