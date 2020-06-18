function check()
{
var i=document.getElementsByTagName("input");
email=i.value;
if(email.lastindexof('.')!=(email.length-3) || email.indexof('@')!=(email.indexof('.')-5))
{
alert("give correct email");
    return false;
}
else
{
   alert("are you sure?");
   return true;
   
 }
 }
