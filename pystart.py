#!F:\python\python.exe
import cgi, cgitb
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Saikat676@',database='db8');
#mydb is pointer of my sql dbms;
cur=mydb.cursor();#for calling cursor

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
username = form.getvalue('username')
password=form.getvalue("password");
if(username==None or password==None):
   print("Content-type:text/html\r\n\r\n")
   print("<html>")
   print("<head>")
   print("<title>my form page</title>");
   print("</head>");
   print("<body>")
   print("<script>")
   print("history.back()");
   print("</script>")

   print("</body>");
   print("</html>");

   
city=form.getvalue("city");
if(form.getvalue('gender')):
   gender=form.getvalue('gender');
bloodgroup=str(form.getvalue("bloodgroup"));

s="insert into web(name,password,gender,course,city)values(%s,%s,%s,%s,%s)";
#smart approach in python
values=(username,password,gender,bloodgroup,city);
cur.execute(s,values);#by this only in curser that will be exicute
mydb.commit();#by this the information will go to data base
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>my form page</title>");
print("</head>");
print("<body>")
print("<script>")
print("window.location.href='registraction.html'");
print("</script>")

print("</body>");
print("</html>");




