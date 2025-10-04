//bai1
{const dx:array[1..3] of shortint=(-1,-1,0);
      dy:array[1..3] of shortint=(0,1,1);
var n,m,i,j,x,y:shortint;
    dem:integer;
    s:array[1..200] of string;
    a:array[0..200,0..200] of string;
    f:text;
    ok:boolean;
function xet(x:integer):string;
begin
 if x mod 2 = 0 then exit(a[n,1]);
 if (x mod 2 <> 0) and (a[n,1] = 'G') then exit('R');
 if (x mod 2 <> 0) and (a[n,1] = 'R') then exit('G');
end;
procedure try(i:integer);
var j:byte;
    k:string;
begin
 if (x=1) and (y=m) then
 begin
  ok:=true;
  exit;
 end;
 for j:=1 to 3 do
 begin
  if (x=1) and (y=m) then
  begin
   ok:=true;
   exit;
  end;
  x:=x+dx[j];
  y:=y+dy[j];
  k:=xet(dem);
  if a[x,y]=k then
  begin
   inc(dem);
   try(i+1);
   dec(dem);
  end;
  x:=x-dx[j];
  y:=y-dy[j];
 end;
end;
begin
 assign(f,'text.inp');reset(f);
 readln(f,n,m);
 for i:=1 to n do readln(f,s[i]);
 for i:=1 to n do
 for j:=1 to m do
  a[i,j]:=copy(s[i],j,1);
 close(f);

 ok:=false;
 dem:=1;
 x:=n;y:=1;
 try(1);

 assign(f,'text.out');rewrite(f);
 if ok then write(f,'TRUE') else write(f,'FALSE');
 close(f);
end.}
//Bai 3 theo pp qui hoạch động
//Bạn có thể giải bài này theo pp quay lui, bài cái túi

{var n,m,i,j,x:integer;
    w,v,kq:array[1..50] of integer;
    t:array[0..50,0..50] of integer;
    f:text;
begin
 assign(f,'text.inp');reset(f);
 readln(f,n,m);
 for i:=1 to n do readln(f,w[i],v[i]);
 close(f);

 for i:=1 to n do
 for j:=0 to m do
 begin
  t[i,j]:=t[i-1,j];
  if (j>=w[i]) and (t[i,j]<t[i-1,j-w[i]]+v[i]) then t[i,j]:=t[i-1,j-w[i]]+v[i];
 end;

 assign(f,'text.out');rewrite(f);
 writeln(f,t[n,m]);
 while n<>0 do
 begin
  if t[n,m]<>t[n-1,m] then
  begin
   inc(x);
   kq[x]:=n;
   m:=m-w[n];
  end;
  dec(n);
 end;
 for i:=x downto 1 do write(f,kq[i],' ');
close(f);
end.}
