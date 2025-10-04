var f:text;
    x,a,b:array[1..100] of integer;
    i,n,m,d:integer;
procedure xuli;
var j,sum,tam:longint;
begin
 sum:=0;//tam:=0;
 for j:=1 to n do
 begin
  inc(sum,a[j]*x[j]);
  //if x[j]=1 then inc(tam);
 end;
 for j:=1 to m do
     if (sum=b[j]) then inc(d);
end;
procedure try(i:integer);
var j:integer;
begin
 for j:=0 to 1 do
 begin
  x[i]:=j;
  if i=n then xuli
   else try(i+1);
 end;
end;
begin
 assign(f,'XDS.inp');reset(f);
 readln(f,n,m);
 for i:=1 to n do read(f,a[i]);
 for i:=1 to m do read(f,b[i]);
 close(f);

 try(1);

 assign(f,'XDS.out');rewrite(f);
 if d=m then
    write(f,1)
 else
    write(f,0);
 close(f);
end.
