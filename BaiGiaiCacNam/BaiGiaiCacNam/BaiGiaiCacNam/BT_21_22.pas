{var f:text;
    a:array[1..1000] of integer;
    n,i,j:integer;
    s,sum:longint;
    ok:boolean;
begin
 assign(f,'text.inp');reset(f);
 readln(f,n);
 for i:=1 to n do
 begin
  read(f,a[i]);
  inc(sum,a[i]);
 end;
 close(f);

 ok:=false;
 if sum mod 2 = 0 then
 for i:=1 to n do
 begin
  inc(s,a[i]);
  if s=(sum div 2) then
  begin
   ok:=true;
   break;
  end;
  if s>(sum div 2) then break;
 end;

 assign(f,'text.out');rewrite(f);
 if ok then write(f,i) else write(f,'0');
 close(f);
end.}
{var f:text;
    n,k,i,j,l,d,s:integer;
    a:array[1..2000] of integer;
    ok:boolean;
begin
 assign(f,'text.inp');reset(f);
 readln(f,n,k);
 for i:=1 to n do read(f,a[i]);
 close(f);

 ok:=false;l:=n;
 for i:=1 to n do
 begin
  s:=0;
  for j:=i to n do
   begin
    if s+a[j]<=k then inc(s,a[j]) else break;
    if (s=k) and (j-i+1<l) then
    begin
     ok:=true;
     d:=i;
     l:=j-i+1;
    end;
   end;
 end;

 assign(f,'text.out');rewrite(f);
 if ok then write(f,d,' ',l) else write(f,'0');
 close(f);
end.}
{var f:text;
    n,m,i,j,x,y:byte;
    min:longint;
    c:array[1..100,1..100] of integer;
    o,a,kq,b:array[1..100] of byte;
function nho(i:byte):integer;
var j:byte;
begin
 nho:=c[i,1];
 for j:=1 to m do
  if c[i,j]<nho then  nho:=c[i,j];
 for j:=1 to m do
  if nho=c[i,j] then
  begin
   b[j]:=b[j]+i;
   break;
  end;
end;
procedure xuli;
var j:byte;
    s,sum:longint;
begin
 s:=0;sum:=0;
 fillchar(b,sizeof(b),0);
 for j:=1 to n do a[j]:=j*o[j];
 for j:=1 to n do inc(s,a[j]);
 if s=n then
 begin
  for j:=1 to n do
   if a[j]<>0 then inc(sum,nho(a[j]));
  if sum<min then
  begin
   min:=sum;
   for j:=1 to m do kq[j]:=b[j]+ kq[j];
  end;
 end;
end;
procedure try(i:byte);
var j:byte;
begin
 for j:=1 downto 0 do
 begin
  o[i]:=j;
  if n=i then xuli
  else try(i+1);
 end;
end;
begin
 assign(f,'text.inp');reset(f);
 readln(f,n,m);
 for i:=1 to n do
 for j:=1 to m do
  read(f,c[i,j]);
 close(f);

 min:=2000000;
 try(1);

 assign(f,'text.out');rewrite(f);
 writeln(f,min);
 for i:=1 to m do writeln(f,kq[i]);
 close(f);
end.}
