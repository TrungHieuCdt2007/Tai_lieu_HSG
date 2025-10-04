program sosatsau;
uses crt;
var N,sum: integer;
    x: array [1..1000] of byte;
    found: boolean;
procedure input;
var f1: text;
    i: byte;
begin
  assign(f1,'DOCAO.INP');
  reset(f1);
  sum := 0;
  read(f1,N);
  for i := 1 to N do
  begin
    read(f1,x[i]);
    inc(sum,x[i]);
  end;
  close(f1);
end;

procedure output;
var f1: text;
    i: byte;
begin
  assign(f1,'DOCAO.OUT');
  rewrite(f1);
  if found then
  begin
    for i := 1 to N do
      write(f1,x[i],' ');
  end
  else
  begin
    write(f1,0);
  end;
  close(f1);
end;

procedure find;
var i,altsum: integer;
begin
  while not found do
  begin
    altsum := 0;
    inc(x[N]);
    if x[1] = 10 then exit;
    for i := N downto 1 do
    begin
      if x[1] = 10 then exit;
      if x[i] > 9 then
      begin
        inc(x[i-1]);
        x[i] := 0;
      end;

    end;
    for i := 1 to N do inc(altsum,x[i]);
    if altsum = sum then found := True;
  end;
end;

begin
  input;
  found := False;
  find;
  output;
end.