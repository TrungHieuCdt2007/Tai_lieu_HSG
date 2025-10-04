//bai 2
{var n,k,j:integer;
    a,b,i,d,dem:longint;
    m:array[1..1000] of longint;
    f:text;
begin
 assign(f,'text.inp');reset(f);
 readln(f,n,k);
 for i:=1 to n do read(f,m[i]);
 read(f,a,b);
 close(f);

 for i:=a to b do
 begin
  d:=0;
  for j:=1 to n do
   begin
    if i mod m[j] = 0 then inc(d);
    if d=k then begin inc(dem);break;end;
   end;
 end;

 assign(f,'text.out');rewrite(f);
 write(f,dem);
 close(f);
end.}
//bai 3
var f:text;
    x,a:array[1..10] of byte;
    //c:array[1..1000] of boolean;
    n,k,i:byte;
    sumt,sum,sumtg:integer;
    ok:boolean;
procedure input;
var     f:text;
        i:longint;
begin
        assign(f,'tnb.inp');
        reset(f);
        readln(f,n,k);
        for i:=1 to n do
        begin
                read(f,a[i]);
                sumt:=sumt+a[i];
        end;
        close(f);
end;

procedure update;
var i:longint;
    fo:text;
begin
    	assign(fo,'tnb.out');
    	append(fo);
    	if sum=sumtg then
    	begin
       		for i:=1 to n do
         			if x[i]=1 then
           			   write(fo,a[i]*x[i],' ');
       		writeln(fo);
    	end;
    	close(fo);
end;
procedure try(i:longint);
var j:longint;
begin
       //if (sum > m) then exit;
       for j:=0 to 1 do
              begin
                      x[i]:=j;
                      sum:=sum + x[i]*a[i]; {sum la tong khoi luong cua cac qua can duoc chon}
                      if i=n then
                                   update
                      else
                                  try(i+1);
                     sum:=sum - x[i]*a[i]; {a[i] la khoi luong cua tung qua qua can}
                 end;
end;

begin
   input;
   ok:=false;
   sumtg:=  sumt div k ;
   if sumt mod k = 0 then
      ok:=true;
   if ok then
       try(1)
       //write(1)
   else

      write(-1);
   readln;
end.


