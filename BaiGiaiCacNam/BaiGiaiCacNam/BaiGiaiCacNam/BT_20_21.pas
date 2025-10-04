//bai1 tốt
{var f:text;
    t,k,i,j,sum,d:integer;
    a:array[1..100] of string;//a la 1 mang ma moi phan tu la kieu chuoi
    ch:char;
begin
 assign(f,'text.inp');reset(f);
 readln(f,t);
 for i:=1 to t do readln(f,a[i]);
 close(f);

 assign(f,'text.out');rewrite(f);
 for k:=1 to t do
 begin
  sum:=0;
  a[k]:=lowercase(a[k]);//bien doi lai thanh chu thuong
  while a[k,1]=' ' do delete(a[k],1,1);//xoa dau cach dau xau
  while a[k,length(a[k])]=' ' do delete(a[k],length(a[k]),1);//xoa dau cach cuoi xau
  while pos(' ',a[k])<>0 do delete(a[k],pos(' ',a[k]),1);//xoa dau cach giua  xau
//trong chuoi nhap vao, ki tu nao co 2 tro len thi dem, sau do tinh tong tat ca lai luu vào bien sum
  for ch:='a' to 'z' do
  begin
   d:=0;
   for i:=1 to length(a[k]) do
    if a[k,i]=ch then inc(d);
   if d>1 then inc(sum,d);
  end;
// trong chuoi nhap vao cac ki tu nao trung lap thi xoa
  for i:=1 to length(a[k]) do
  begin
   j:=i+1;
   repeat
    if a[k,i]=a[k,j] then delete(a[k],j,1)
     else inc(j);
   until j>length(a[k]);
  end;
  writeln(f,sum,' ',a[k]);
 end;
 close(f);
end.}
//bai2 có thể sử dụng thuật toán quay lui bài toán ATM mỗi tờ lấy nhiều lần thay vì 1 lần
{var f:text;
     a,l,mg,slg:array[1..50] of integer;
     n,t,i,j,x,d:integer;
     ok:boolean;
begin
 assign(f,'text.inp');reset(f);
 readln(f,n,t);
 for i:=1 to n do readln(f,a[i],l[i]);
 close(f);

 ok:=false;
 for i:=n downto 1 do
 begin
  for j:=l[i] div 2 downto 1 do
   if (a[i]*2*j)<=t then
   begin
    t:=t-a[i]*2*j;
    inc(x);
   mg[x]:=a[i];slg[x]:=j*2;
   end;
   if t=0 then ok:=true;
 end;

 assign(f,'text.out');rewrite(f);
 if ok then
  for i:=x downto 1 do writeln(f,mg[i],' ',slg[i])
 else write(f,'0');
 close(f);
end.}
//bai3 tốt
{var n,d,i,j,tam,time,sum,max:integer;
    t,z:array[1..50] of integer;
    f:text;
begin
 assign(f,'text.inp');reset(f);
 readln(f,n,d);
 for i:=1 to n do read(f,t[i]);
 for i:=1 to n do read(f,z[i]);
 close(f);
//nho sap xep QS nha
 for i:=1 to n-1 do
 for j:=i+1 to n do
  if t[i]>t[j] then
  begin
   tam:=t[i];t[i]:=t[j];t[j]:=tam;
   tam:=z[i];z[i]:=z[j];z[j]:=tam;
  end;
 for i:=1 to n do
 begin
  time:=0;sum:=0;
  for j:=i to n do
   if t[j]-time>=d then
   begin
    inc(time,d);
    inc(sum,z[j]);
   end;
  if max<sum then max:=sum;
 end;

assign(f,'text.out');rewrite(f);
write(f,max);
close(f);
end.}
