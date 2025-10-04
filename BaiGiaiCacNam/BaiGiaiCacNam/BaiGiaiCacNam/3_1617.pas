var f:text;
    n,m,i,j,hv,hcn,d:integer;
    m2c:array[0..50,0..50] of byte;
function  kt_hv(x,y,d:integer):integer;
var q,e,p,d_hv:integer;
begin
 //for e:=d downto 2 do
  d_hv:=0;
  //kt_hv:=0;
  if d>1 then
  begin
      for q:=x to x+d-1 do
      for p:=y to y+d-1 do
          if (m2c[q,p]=1) then inc(d_hv);
      if d_hv=sqr(d)  then
           kt_hv:=d*d

      else
           kt_hv:=0;
  end
  else
      kt_hv:=0;
end;
function kt_hcn(x,y,e,w:integer):integer;
var q,p,d_hcn:integer;
begin
   d_hcn:=0;
  for q:=x to x+w-1 do
     for p:=y to y+e-1 do
        if m2c[q,p]=1 then inc(d_hcn);
   if d_hcn=e*w then
   begin
        kt_hcn:=e*w;
   end
   else
      kt_hcn:=0;
end;
procedure kt(x,y:integer);
var dthcn,dthcnm,dai,rong,q,e,wm,p,dthv,dthvm,emv,w,emn:integer;
    co:boolean;
begin
 dthcnm:=0;
 dthvm:=0;
 dthv:=0;
 dthcn:=0;
 dai:=1;rong:=1;
 q:=x;p:=y;
 while m2c[x,p]=1 do
 begin
     inc(p);inc(dai);
 end;
 while m2c[q,y]=1 do
 begin
     inc(q);inc(rong);
 end;
 for e:=dai-1 downto 1 do
 for w:=rong-1 downto 1 do
 begin
   if e<>w then
   begin
        dthcn:=kt_hcn(x,y,e,w);
        if dthcn>dthcnm then
        begin
             dthcnm:=dthcn;
             emn:=e;
             wm:=w;
        end
        else
             dthcnm:=dthcnm;
   end
   else
   begin
       dthv:=kt_hv(x,y,e);
       if dthv > dthvm then
       begin
            dthvm:=dthv;
            emv:=e;
       end
       else
            dthvm:=dthvm;
   end;
end;

if  (dthcnm>dthvm)  then
   begin
      inc(hcn);
      for q:=x to x+wm-1 do
      for p:=y to y+emn-1 do
         m2c[q,p]:=0;
      exit;
  end;
if (dthvm>dthcnm)then
  begin
      inc(hv);
      for q:=x to x+emv-1 do
      for p:=y to y+emv-1 do
            m2c[q,p]:=0;
      exit;
  end;
end;
begin
 assign(f,'CNMAX.inp');reset(f);
 readln(f,n,m);
 for i:=1 to n do
 for j:=1 to m do
      read(f,m2c[i,j]);
 close(f);

 for i:=1 to n do
 for j:=1 to m do
      if (m2c[i,j]=1) then kt(i,j);

 assign(f,'CNMAX.out');rewrite(f);
 writeln(f,hv);
 writeln(f,hcn);
 close(f);
end.
