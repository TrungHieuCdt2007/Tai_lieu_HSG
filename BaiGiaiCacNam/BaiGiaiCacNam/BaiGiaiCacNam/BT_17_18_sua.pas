//bai 1
{var n,m,k,i:integer;
    fi,fo:text;
function snt(x:integer):boolean;
var o:integer;
begin
 snt:=true;
 if x<2 then snt:=false;
 for o:=2 to x div 2 do
  if x mod o = 0 then snt:=false;
end;
function kt(a,b:integer):boolean;
var sa,sb,da,db,j:integer;
begin
 kt:=false;sa:=0;da:=0;sb:=0;db:=0;
 for j:=1 to a div 2 do
  if (a mod j = 0) and (snt(j)) then begin inc(sa,j);inc(da);end;
 for j:=1 to b div 2 do
  if (b mod j = 0) and (snt(j)) then begin inc(sb,j);inc(db);end;
 if (da=db) and (sa=sb) then kt:=true;
end;
begin
 assign(fi,'text.inp');reset(fi);
 assign(fo,'text.out');rewrite(fo);

 repeat
  readln(fi,n,m);
  if  (n<>0) and (m<>0) then
   if kt(n,m) then writeln(fo,'1') else writeln(fo,'0');
 until (n=0) and (m=0);
 close(fi);
 close(fo);
end.}


//bai 2
// bai 27 trang 70,71 trong tai lieu 100 de toan tin
{var d,i,j,max,x,y:integer;
    a:array[1..8,1..8] of integer;
    f:text;
begin
 assign(f,'text.inp');reset(f);
 for i:=1 to 8 do
 for j:=1 to 8 do
  read(f,a[i,j]);
 close(f);

 // cheo trai
 for i:=1 to 15 do
 begin
  d:=0;
  if i<=8 then x:=i else x:=8;
  if i<=8 then y:=1 else y:=i-7;
  for j:=1 to x-y+1 do
  begin
   if a[x,y]=1 then
   begin
    inc(d);
    if d>max then max:=d;
   end else d:=0;
   dec(x);inc(y);
  end;
 end;
 // cheo phai
 for i:=1 to 15 do
 begin
  d:=0;
  if i<=8 then x:=1 else x:=i-7;
  if i<=8 then y:=9-i else y:=1;
  for j:=1 to 8-abs(x-y) do
  begin
   if a[x,y]=1 then
   begin
    inc(d);
    if d>max then max:=d;
   end else d:=0;
   inc(x);inc(y);
  end;
 end;
 // ngang
 for i:=1 to 8 do
 begin
  d:=0;
  for j:=1 to 8 do
   if a[i,j]=1 then
   begin
    inc(d);
    if d>max then max:=d;
    end else d:=0;
   end;
 //doc
 for i:=1 to 8 do
 begin
  d:=0;
  for j:=1 to 8 do
   if a[j,i]=1 then
   begin
    inc(d);
    if d>max then max:=d;
   end else d:=0;
 end;

 assign(f,'text.out');rewrite(f);
 write(f,max);
 close(f);
end.}
//bai 3
{var f:text;
    n,m,i,j,dem:integer;
    a,b:array[1..40,1..40] of byte;
function kt(x,y:byte):boolean;
var d,k,l:integer;
begin
 d:=0;
 for k:=x to x+m-1 do
 for l:=y to y+m-1 do
  if a[k,l]=b[k-x+1,l-y+1] then inc(d) else exit(false);
 if d=sqr(m) then kt:=true else kt:=false;
end;
begin
 assign(f,'text.inp');reset(f);
 readln(f,n,m);
 for i:=1 to m do
 for j:=1 to m do
  read(f,b[i,j]);
 for i:=1 to n do
 for j:=1 to n do
  read(f,a[i,j]);
 close(f);

 for i:=1 to n-m+1 do
 for j:=1 to n-m+1 do
  if (kt(i,j)) and (a[i,j]=b[1,1]) then inc(dem);

 assign(f,'text.out');rewrite(f);
 write(f,dem);
 close(f);
end.}
