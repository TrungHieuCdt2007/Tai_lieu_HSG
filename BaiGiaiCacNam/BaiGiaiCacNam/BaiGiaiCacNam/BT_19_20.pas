//bai1;
{var f:text;
    n,k,q:integer;
begin
 assign(f,'text.inp');reset(f);
 read(f,n,k);
 close(f);

 assign(f,'text.out');rewrite(f);
 if k<=round((n+0.1)/2) then write(f,1+2*(k-1))
  else write(f,2+2*(k-round((n+0.1)/2)-1));
 close(f);
end.}
//bai2
{var f:text;
    n,i,j,x:byte;
    s,p,st,mahoa:string;
begin
 assign(f,'text.inp');reset(f);
 readln(f,n);
 readln(f,p);
 readln(f,s);
 close(f);

 x:=1;
 repeat
  st:=copy(s,x,n);
  while length(st)<>n do st:=st+' ';
  for i:=1 to n do
  begin
   val(p[i],j);
   mahoa:=mahoa+st[j];
  end;
  inc(x,n);
 until x>length(s);

 assign(f,'text.out');rewrite(f);
 write(f,mahoa);
 close(f);
end.}
//bai3
var n,k,i,j,sum,max,x:integer;
    a,b:array[1..50] of integer;
    f:text;
begin
        assign(f,'text.inp');reset(f);
        readln(f,n,k);
        for i:=1 to n do read(f,a[i]);
        for i:=1 to n do read(f,b[i]);
        close(f);

        for i:=1 to n do
        begin
         x:=1;
         sum:=b[1];
         if i<>n then
         begin
          for j:=i+1 to n-1 do
           if (a[j]-a[x])>=k then
           begin
            inc(sum,b[j]);
            x:=j;
           end;
          inc(sum,b[n]);
         end;
		if sum>max then max:=sum;
        end;

        assign(f,'text.out');rewrite(f);
        write(f,max);
        close(f);
end.
