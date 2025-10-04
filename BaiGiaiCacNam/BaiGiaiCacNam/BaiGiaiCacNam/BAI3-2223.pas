program bandia;
uses crt;
var N: byte;
    a: array [1..1000] of integer;
    x: array [1..1000] of byte;
    mainscore,score: longint;
procedure input;
var f1: text;
    i: byte;
begin
  assign(f1,'GAME.INP');
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
  assign(f1,'GAME.OUT');
  rewrite(f1);
  write(f1,mainscore);
  close(f1);
end;

procedure update;
begin
  if score > mainscore then mainscore := score;
end;

procedure Try(i: integer; ammo: integer);
var j: byte;
begin
  for j := 0 to 1 do
  begin
    x[i] := j;
    inc(score,a[i] * x[i]);
    if ammo = 0 then
    begin
      if j = 0 then
      begin
        if i = n then update
        else Try(i+1,2);
        dec(score,a[i] * x[i]);
      end
      else
      begin
        dec(score,a[i] * x[i]);
        exit;
      end;
    end
    else
    begin
      if j = 0 then
      begin
        if i = n then update
        else Try(i+1,2);
        dec(score,a[i] * x[i]);
      end
      else
      begin
        if i = n then update
        else Try(i+1,ammo - 1);
        dec(score,a[i] * x[i]);
      end;
    end;

  end;
end;

begin
  input;
  mainscore := 0;
  score := 0;
  Try(1,2);
  output;
end.