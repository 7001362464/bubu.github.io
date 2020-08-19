
var button1=document.querySelector("#d");
var button2=document.querySelector("#f");
var button3=document.querySelector("#t");
var pofp=document.querySelector("#pofp");
var posp=document.querySelector("#posp");
var par=document.querySelector("p");
var input=document.querySelector("input");


p1s=0;
p2s=0;
limit=5;
stop=false;


button1.addEventListener("click", function() {
if(!stop)
{
p1s+=1;
 pofp.textContent=p1s;
 if(p1s===limit)
 {
 stop=true;

 pofp.classList.add("winner");
 par.textContent="1st player is winner"

 }
 }
});
button2.addEventListener("click", function() {
if(!stop)
{
p2s+=1;
 posp.textContent=p2s;
 if(p2s===limit)
 {
 stop=true;
 posp.classList.add("winner");
 par.textContent="2nd player is winner"
 }
 }
});
button3.addEventListener("click", function() {
p1s=0;
p2s=0;
stop=false;
pofp.textContent=p1s;
posp.textContent=p2s;
pofp.classList.remove("winner");
posp.classList.remove("winner");
par.textContent="playing to "+limit+":";

});
input.addEventListener("change", function() {
get=Number(input.value);
limit=get;
p1s=0;
p2s=0;
stop=false;
pofp.textContent=p1s;
posp.textContent=p2s;
pofp.classList.remove("winner");
posp.classList.remove("winner");
par.textContent="playing to "+get+":";

});


