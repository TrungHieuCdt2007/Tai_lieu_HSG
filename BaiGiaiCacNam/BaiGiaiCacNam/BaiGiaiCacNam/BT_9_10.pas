//bai 2
var m:byte;
    i,j,k,n,d,next:integer;
    a:array[1..1000] of string;
    s,st:string;
    f:text;
begin
 assign(f,'text.inp');reset(f);
 readln(f,m);
 readln(f,s);
 repeat
  inc(i);
  readln(f,a[i]);
 until a[i]='';
 n:=i-1;
 close(f);

 assign(f,'text.out');rewrite(f);
 for i:=1 to n do
 begin
  st:='';next:=1;
  for j:=1 to length(s) do
  begin
   for k:=next to length(a[i]) do
   if s[j]=a[i,k] then
   begin
    next:=k+1;
    st:=st+a[i,k];
    break;
   end;
   if (st=s) and ((100-(length(s)*100) div length(a[i]))<=m) then
   begin
    inc(d);
    if d=1 then writeln(f,s);
    write(f,a[i],' ');
   end;
  end;
 end;
 if d=0 then write(f,d);
 close(f);
end.