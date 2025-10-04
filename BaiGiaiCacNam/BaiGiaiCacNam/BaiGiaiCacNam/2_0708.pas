Program dulich;
var c:array[1..1000,1..1000] of longint;
    x,xs:array[1..1000] of longint;
    d:array[1..1000] of longint;
    n:longint;
    ok:boolean;
procedure input;
var f:text;
    i,j:longint;
begin
   assign(f,'tsp.inp');
   reset(f);
   read(f,n);
   for i:=1 to n do
      for j:=1 to n do
        read(f,c[i,j]);
   close(f);
end;
procedure update;
var i:longint;
begin
       xs:=x;
       ok:=true;
end;
procedure try(i:longint);
var j:longint;
begin
    if ok  then exit;
    for j:=1 to n do
         if (d[j]=0) and (c[x[i-1],j]=0) then
               begin
                      x[i]:=j;
                      d[j]:=1;
                      if i=n then
                            update
                      else
                            try(i+1);
                     d[j]:=0;
                end;
end;

procedure print;
var i:longint;
begin
       for i:=1 to n do
           write(xs[i],' ');
end;
begin
   input;
   fillchar(d,sizeof(d),0);
   ok:=false;
   x[1]:=1;
   d[1]:=1;
   try(2);
   print;
   readln;
end.
