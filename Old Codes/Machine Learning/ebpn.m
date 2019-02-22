x = [0.1 0.1; 0.1 0.9; 0.9 0.1; 0.9 0.9];
t = [0.1 0.9 0.9 0.1];
v = [0 0 0 0];
w = [0 0];
b1 = 0; b2 = 0; b3 = 0;
for c=1:100
fprintf('ITERATION %d\n', c);
for i=1:4
    net21 = x(i, 1) * v(1) + x(i, 2) * v(2) + b1;
    net22 = x(i, 1) * v(3) + x(i, 2) * v(4) + b2;
    out21 = 1 / (1 + exp(-net21));
    out22 = 1 / (1 + exp(-net22));
    net31 = out21 * w(1) + out22 * w(2) + b3;
    out31 = 1 / (1 + exp(-net31));
    if out31 ~= t(i)
        dw1 = 0.7 * out21 * (t(i) - out31) * out31 * (1 - out31);
        dw2 = 0.7 * out22 * (t(i) - out31) * out31 * (1 - out31);
        w(1) = w(1) + dw1;
        w(2) = w(2) + dw2;
        b3 = b3 + 0.7 * (t(i) - out31) * out31 * (1 - out31);
        dv1 = 0.7 * x(i, 1) * (t(i) - out31) * out31 * (1 - out31) * (w(1) + w(2)) * out21 * (1 - out21);
        dv2 = 0.7 * x(i, 2) * (t(i) - out31) * out31 * (1 - out31) * (w(1) + w(2)) * out21 * (1 - out21);
        dv3 = 0.7 * x(i, 1) * (t(i) - out31) * out31 * (1 - out31) * (w(1) + w(2)) * out22 * (1 - out22);
        dv4 = 0.7 * x(i, 2) * (t(i) - out31) * out31 * (1 - out31) * (w(1) + w(2)) * out22 * (1 - out22);
        v(1) = v(1) + dv1;
        v(2) = v(2) + dv2;
        v(3) = v(3) + dv3;
        v(4) = v(4) + dv4;
        b1 = b1 + 0.7 * (t(i) - out31) * out31 * (1 - out31) * (w(1) + w(2)) * out21 * (1 - out21);
        b2 = b2 + 0.7 * (t(i) - out31) * out31 * (1 - out31) * (w(1) + w(2)) * out22 * (1 - out22);
    end
    fprintf('For input %d, output is: %0.3f\n', i, out31);
    disp(w);
    disp(v);
end
end