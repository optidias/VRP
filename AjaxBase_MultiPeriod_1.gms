Option optcr=0

Sets
i product /1*3/
j lines /1*2/
t weeks /w1,w2,w3,w4/
;

Parameters
L(i) labor hours of product i
/1 10
 2 15
 3 20/

TE(i) testing hours of product i
/1 1
 2 1
 3 1/

V(i) net profit of product i
/1 350
 2 470
 3 610/

R(j) max capacity of line j
/1 120
 2 48/

LP(i,j) if product i is tested in line j
/1.1=1
 1.2=0
 2.1=1
 2.2=0
 3.1=0
 3.2=1/

C(i) inventory holding cost of product i
/1 9
 2 10
 3 18/

SI(i) initial inventory of product i
/1 22
 2 42
 3 36/

;

Table SMi(i,t) Minimum sales of product i at week t
    w1  w2  w3  w4
1   20  20  20  20
2   20  20  20  20
3   20  20  20  20
;
Table SMa(i,t) Maximum sales of product i at week t
    w1  w2   w3   w4
1   60  80  120  140
2   40  40  40   40
3   50  40  30   70   ;


Scalar
H labor hours for product assembly /2000/;

Variables
N(i,t) number of product i to assemble test and sell in week t
S(i,t)  sales of product i in week t
IV(i,t) final inventory of product i in week t
Z
;


*Positive variables N, S, IV;
Integer variables N, S, IV;

S.lo(i,t)=SMi(i,t);
S.up(i,t)=SMa(i,t);

Equations
NetProfit
Line(j,t)
Labour(t)
*SalesMin(i,t)
*SalesMax(i,t)
Inventory(i,t)
InitialInventory(i,t)
;

NetProfit.. Z=e=sum((i,t),S(i,t)*V(i))-sum((i,t)$(ord(t)<=3),IV(i,t)*C(i))+ sum(i,IV(i,'w4')*(V(i)-4*C(i)));

Line(j,t).. sum(i,TE(i)*N(i,t)*LP(i,j))=l=R(j);

Labour(t).. sum(i,N(i,t)*L(i))=l=H;

*SalesMin(i,t).. S(i,t)=g=SMi(i,t);
*SalesMax(i,t).. S(i,t)=l=SMa(i,t);

InitialInventory(i,t)$(ord(t)=1)..  IV(i,t)=e=SI(i)+N(i,t)-S(i,t);

Inventory(i,t)$(ord(t)>=2).. IV(i,t)=e=IV(i,t-1)+N(i,t)-S(i,t);


Model AjaxMulti /all/;

Solve AjaxMulti using mip maximize z;

Display n.l, s.l, iv.l;





