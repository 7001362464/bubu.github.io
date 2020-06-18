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
result1 = "SELECT password,name FROM web;"
cur.execute(result1);
result=cur.fetchall()
for i in result:
    if(i[0]==password and i[1]==username):
      mydb=mysql.connector.connect(host='localhost',user='root',password='Saikat676@',database='db8');
#mydb is pointer of my sql dbms;
      cur=mydb.cursor();#for calling cursor
      values=(username,password);
      result1 = "SELECT result FROM web WHERE name = %s AND password = %s;"
      cur.execute(result1,values);
      result=cur.fetchall()
      result=result[0][0];
      mydb.commit()
      print("Content-type:text/html\r\n\r\n")
      print("<html>")
      print("<head>")
      print("<title>Hello - Second CGI Program</title>")
      print("</head>")
      print("<body>")
      print("<p>your latest result is-> {} </p>".format(result));
      print("<form action='new4.html' method='get'>");
      print("<table>");
      print("<p>if want to update your result click on update button</p>");
    
     



      print("<tr>");
      print("<td><input type='submit' value='update'/></td>");
      print("</tr>");
      print("</table>");
      print("</form>");



      print("</body>");
      print("</html>");
      break;
      
else:
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>Hello - Second CGI Program</title>")
    print("</head>")
    print("<body>")
     
    print("<script>");
    print("window.location.href='savewrong.html'");
    print("</script>");
      
    print("</body>");
    print("</html>");
    

    
