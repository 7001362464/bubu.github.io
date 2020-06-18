#!F:\python\python.exe
import cgi, cgitb
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Saikat676@',database='db8');
#mydb is pointer of my sql dbms;
cur=mydb.cursor();#for calling cursor

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
sym1= form.getvalue('symptoms1')
sym2=form.getvalue("symptoms2");

        
    

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("<link rel='stylesheet' type='text/css' href='save5.css'/>")
print("</head>")
print("<body>")
print("<form action='new4.html' method='get'>")
print("<table>");
print("<h1 style='background-color:pink'>your Result</h1>");

if(sym1 and sym2):
    if(type(sym1) is not str or type(sym2) is not str):
        if(type(sym1)==str):
            sym1=[sym1];
        elif(type(sym2)==str):
            sym2=[sym2];
        if(len(sym1)>1 or len(sym2)>3):
          print("<p>your chance to be affected in coronavirus is 80% to 100%!!!!</p>");
          result="your chance to be affected in coronavirus is 80% to 100%!!!!"
          print("<p>suggetion:alert!stay at home and call immidiately 1800313444222/03323412600 on any of this no</p>")
        elif(len(sym2)==2):
          print("<p>your chance to be affected in coronavirus is 30% to 40%!!!!</p>");
          result="your chance to be affected in coronavirus is 30% to 40%!!!!"
          print("<p>Go to a doctor </p>");
        else:
          print("<p>your chance to be affected in coronavirus is 50% to 60%!!!!</p>");
          result="your chance to be affected in coronavirus is 50% to 60%!!!!"
          print("<p>call on 911123978046 this no </p>");
    else:
        print("<p>your chance to be affected in coronavirus is 10% to 20%!!!!</p>");
        result="your chance to be affected in coronavirus is 10% to 20%!!!!"
        print("<p>keep updating your situation in our app</p>");
elif(sym1):
    if(len(sym1)==3):
         print("<p>your chance to be affected in coronavirus is 50% to 70%!!!!</p>");
         result="your chance to be affected in coronavirus is 50% to 70%!!!!"
         print("<p>Go to a doctor </p>");
    else:
        print("<p>your chance to be affected in coronavirus is 10% to 20%!!!!</p>");
        result="your chance to be affected in coronavirus is 10% to 20%!!!!"
        print("<p>keep updating your situation in our app</p>");
elif(sym2):
    if(len(sym2)==5):
        print("<p>your chance to be affected in coronavirus is 50% to 70%!!!!</p>");
        result="your chance to be affected in coronavirus is 50% to 70%!!!!"
        print("<p>Go to a doctor </p>");
    else:
         print("<p>your chance to be affected in coronavirus is 10% to 20%!!!!</p>");
         result="your chance to be affected in coronavirus is 10% to 20%!!!!"
         print("<p>keep updating your situation in our app</p>");
else:
    print("<p>your chance to be affected in coronavirus is 10% to 20%!!!!</p>");
    result="your chance to be affected in coronavirus is 10% to 20%!!!!"
    print("<p>keep updating your situation in our app</p>");
    


         


print("<tr>");
print("<td><input type='submit' value='back'/></td>")
    
print("</tr>");

print("</table>");
print("</form>");
print("<p>to save result give password,username,result and click the save button</p>");

print("<form action='new4.py' method='get'>")
print("<table>");
    
print("<tr>")
print("<td>name</td>");
print("<td><input type='text' name='username'/></td>");
print("</tr>");
print("<tr>")
print("<td>password</td>");
print("<td><input type='password' name='password' /></td>");
print("</tr>");
print("<tr>")
print("<td>type the above result</td>");
print(("<td><input type='text' name='result'/></td>"));
print("</tr>");

         


print("<tr>");
print("<td><input type='submit' value='save'/></td>")
    
print("</tr>");

print("</table>");
print("</form>");
print("<h1 style='font-family:courier;background-color:white'>this website is created by saikat mondal</h1>");
print("<img width=40% height=25% border='8px' src='bubai.jpg' alt='Smiley face' align='right'>");


      
      

    
        
        
        
          
          
            
            
   
print("</body>")
print("</html>")



