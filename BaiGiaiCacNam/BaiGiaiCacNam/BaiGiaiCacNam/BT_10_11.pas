//bai 2
{var f:text;
    n,m,i:byte;
    a:array[1..100] of integer;
function kt(x:byte):boolean;
var d,c,j:byte;
begin
 kt:=true;
 if x-m>=1 then d:=x-m else d:=1;
 if x+m<=n then c:=x+m else c:=n;
 for j:=d to c do
  if a[x]<a[j] then exit(false);

end;
begin
 assign(f,'text.inp');reset(f);
 readln(f,n,m);
 for i:=1 to n do read(f,a[i]);
 close(f);

 assign(f,'text.out');rewrite(f);
 for i:=1 to n do
  if kt(i) then write(f,a[i],' ');
 close(f);
end.}
//bai 3
var f:text;
    n,i,j,d:byte;
    s,tam,s1,s2:string;
    a,vt1,vt2:array[1..120] of byte;
begin
 assign(f,'text.inp');reset(f);
 readln(f,n);
 for i:=1 to n do read(f,a[i]);
 close(f);

 for i:=1 to n do
 begin
  str(a[i],tam);
  s:=s+tam;
 end;
 s:=s+s;
 for i:=n div 2 to n + n div 2 - 1 do
 begin
  s2:='';
  s1:=copy(s,i - n div 2 + 1,n div 2);
  tam:=copy(s,i+1,n div 2);
  for j:=n div 2 downto 1 do
   s2:=s2+tam[j];
  if s1=s2 then
  begin
   inc(d);
   vt1[d]:=i- n div 2;
   vt2[d]:=vt1[d]+1;
  end;
 end;
 assign(f,'text.out');rewrite(f);
 if n mod 2 = 0 then
 begin
  writeln(f,d);
  for i:=1 to d do writeln(f,vt1[i],' ',vt2[i]);
 end else write(f,'KHONG CO');
 close(f);
end.