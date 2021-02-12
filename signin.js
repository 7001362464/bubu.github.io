k=document.querySelectorAll("div[class='triangle-left']");
c=document.querySelectorAll("div[class='circle']");
s=[[20,250],[30,1160],[810,820],[110,990],[140,840],[570,870]];

s1=[[280,334],[780,1000],[530,1050]];
for(i=0;i<k.length;i++)
{

k[i].style.marginTop=`${s[i][0]}px`;
k[i].style.marginLeft=`${s[i][1]}px`;
k[i].style.transform=`rotate(5deg)`;



}

for(i=0;i<c.length;i++)
{

c[i].style.marginTop=`${s1[i][0]}px`;
c[i].style.marginLeft=`${s1[i][1]}px`;
if(i>0)
{

c[i].style.width=`100px`;
c[i].style.height=`100px`;
;


}

}