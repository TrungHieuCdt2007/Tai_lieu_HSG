//bai 1
{uses crt;
var f:text;
    nx,dx,nd,dd,nt,dt,nv,dv:longint;
    a,b:int64;
function ucln(x,y,i,j:longint):int64;
begin
 while x<>y do
  if x>y then dec(x,i) else dec(y,j);
 ucln:=x;
end;
begin
 assign(f,'text.inp');reset(f);
 readln(f,nx,dx);
 readln(f,nd,dd);
 readln(f,nt,dt);
 readln(f,nv,dv);
 close(f);

 assign(f,'text.out');rewrite(f);
 a:=ucln(nx*dx,nt*dt,dx,dt);
 b:=ucln(nd*dd,nv*dv,dd,dv);
 writeln(f,a*b);
 write(f,a/dx:0:0,' ',b/dd:0:0,' ',a/dt:0:0,' ',b/dv:0:0);
 close(f);
end.}
//bai 2
{var f:text;
    a,b,sum:longint;
procedure xuli(x:longint);
var mang:array[1..100] of longint;
    s,st:string;
    tam,n,i,j,k,d:word;
begin
 n:=1;
 fillchar(mang,sizeof(mang),0);
 inc(sum,x);
 str(x,s);
 for i:=1 to length(s)-1 do
 for j:=1 to length(s)-i+1 do
 begin
  d:=0;
  st:=copy(s,j,i);
  val(st,tam);
  for k:=1 to n do
   if tam<>mang[k] then inc(d) else break;
  if d=n then
  begin
   inc(n);
   mang[n]:=tam;
   inc(sum,tam);
  end;
 end;
end;
begin
 assign(f,'text.inp');reset(f);
 readln(f,a);
 read(f,b);
 close(f);

 xuli(a);
 xuli(b);

 assign(f,'text.out');rewrite(f);
 write(f,sum);
 close(f);
end.}
//bai 3
{var f:text;
    n,i,sum:integer;
    k:byte;
    a,x:array[1..1000] of integer;
    ok:boolean;
procedure try(i:integer);
var j:integer;
begin
 for j:=1 to 2 do
 begin
  x[i]:=j;
  if x[i]=1 then inc(sum,a[i]) else dec(sum,a[i]);
  if i=n then
  begin
   if sum mod k = 0 then ok:=true;
  end else try(i+1);
  if ok then exit;
  if x[i]=1 then dec(sum,a[i]) else inc(sum,a[i]);
 end;
end;
begin
 assign(f,'text.inp');reset(f);
 readln(f,n,k);
 for i:=1 to n do read(f,a[i]);
 close(f);

 ok:=false;
 sum:=a[1];
 try(2);

 assign(f,'text.out');rewrite(f);
 if ok then
 begin
  writeln(f,'1');
  write(f,a[1]);
  for i:=2 to n do
   if x[i]=1 then write(f,'+',a[i]) else write(f,'-',a[i]);
  write(f,'=',sum);
 end else writeln(f,'0');
 close(f);
end.}