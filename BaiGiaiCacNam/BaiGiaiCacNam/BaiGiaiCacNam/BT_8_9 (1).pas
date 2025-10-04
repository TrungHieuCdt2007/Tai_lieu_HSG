//bai 1
{var f:text;
    n:byte;
    i,ka,kb,k,cs:byte;
    a,b:array[1..1000] of int64;
function kt(x:int64):boolean;
var j:longint;
begin
 kt:=false;
 if x<2 then exit;
 for j:=2 to x div 2 do
  if x mod j = 0 then exit;
 kt:=true;
end;
function snt(x:int64):boolean;
begin
 snt:=false;
 while kt(x) do x:=x div 10;
 if x=0 then snt:=true;
end;
begin
 assign(f,'text.inp');reset(f);
 read(f,n);
 close(f);

 ka:=1;
 for i:=1 to n do
 begin
  kb:=0;
  for k:=1 to ka do
   for cs:=0 to 9 do
    if kt(a[k]*10+cs) then
    begin
     kb:=kb+1;
     b[kb]:=a[k]*10+cs;
    end;
  ka:=kb;
  for k:=1 to ka do
   a[k]:=b[k];
 end;

 assign(f,'text.out');rewrite(f);
 writeln(f,ka);
 for i:=1 to ka do write(f,a[i],' ');
 close(f);
end.}
//bai 2
{var n,m,i:byte;
    s,st:string;
    f:text;
begin
 assign(f,'text.inp');reset(f);
 readln(f,n,m,s);
 read(f,st);
 close(f);

 delete(s,1,1);
 while length(st)<>m do
 begin
  inc(i);
  if st[i]<>s then st:=st+st[i];
  if i=n then i:=0;
 end;

 assign(f,'text.out');rewrite(f);
 writeln(f,m);
 write(f,st);
 close(f);
end.}
