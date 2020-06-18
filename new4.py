#!F:\python\python.exe
import cgi, cgitb
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Saikat676@',database='db8');
#mydb is pointer of my sql dbms;
cur=mydb.cursor();#for calling cursor

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
username= form.getvalue('username')
password=form.getvalue("password");
result=form.getvalue("result");
values=(result,password);
s="update web set result=%s where password=%s";
cur.execute(s,values);
mydb.commit()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("<link rel='stylesheet' type='text/css' href='save5.css'/>");
print("</head>")
print("<body>")
print("<p>you result is saved successfully</p>")
print("<form action='save5.html' method='get'>");
print("<table>");
print("<p>click on home page to go home page</p>");
    
     



print("<tr>");
print("<td><input type='submit' value='home page'/></td>");
print("</tr>");
print("</table>");
print("</form>");
print("<h1 style='font-family:courier;background-color:white'>this website is created by saikat mondal</h1>");
print("<img width=40% height=25% border='8px' src='bubai.jpg' alt='Smiley face' align='right'>");


print("</body>");
print("</html>");




