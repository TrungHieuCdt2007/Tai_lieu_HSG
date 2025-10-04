var n:integer;
    co:boolean;
    a:array[1..1000] of char;
procedure swap(x,y:integer);
var tam:char;
begin
 tam:=a[x];
 a[x]:=a[y];
 a[y]:=tam;
end;
procedure input;
var fi:text;
    vt:integer;
begin
    assign(fi,'sosatsau.inp');
    reset(fi);
    readln(fi,n);
    for vt:=1 to n do
        read(fi,a[vt]);
    close(fi);
end;
procedure sapxep(x:integer);
var i,j:byte;
begin
 for i:=x to n-1 do
 for j:=i+1 to n do
    swap(i,j);
end;
procedure xuli;
var vt,k,p:integer;
begin
    co:=true;
    vt:=n-1;
    while (vt>0) and(a[vt]>a[vt+1]) do
         vt:=vt-1;
    if vt=0 then
    begin
       co:=false;
       exit();
    end;
    k:=vt;
    p:=n;
    while a[p] <a[k]  do
         p:=p-1;
    swap(k,p);
    sapxep(vt+1);
end;
procedure output;
var fo:text;
    vt:integer;
begin
    assign(fo,'sosatsau.out');
    rewrite(fo);
    if co then
        for vt:=1 to n do
           write(fo,a[vt])
    else
        write(fo,0);
    close(fo);
end;
begin
  input;
  xuli;
  output;
end.
