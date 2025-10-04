program chuoi;
uses crt;
var a: array [1..100] of byte;
    N: byte;
    b: array [1..30] of boolean;
function dem: byte;
var i,c: byte;
begin
  c := 0;
  for i := 1 to n do
    if not( b[a[i]] ) then
    begin
      inc(c);
      b[a[i]] := True;
    end;
  dem := c;
end;

procedure input;
var f1: text;
    i: byte;
begin
  assign(f1,'CHUOI.INP');
  reset(f1);
  read(f1,N);
  for i := 1 to N do
    read(f1,a[i]);
  close(f1);
end;

procedure output;
var f1: text;
    i: byte;
begin
  assign(f1,'CHUOI.OUT');
  rewrite(f1);
  if n = 2 then
  begin
    writeln(f1,a[1],' ',a[2]);
    exit;
  end;
  write(f1,a[1],' ');
  for i := 1 to trunc(n/2)-1 do
    write(f1,a[2*i+1],' ');
  if n mod 2 <> 0 then write(f1,a[n],' ');
  for i := trunc(n/2) downto 1 do
    write(f1,a[2*i],' ');
  writeln(f1);
  write(f1,dem);
  close(f1);
end;
begin
  input;
  output;
end.