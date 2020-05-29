# Blasius-Profile
Blasius equation: $f^{'''}+0.5ff^{''}$

with boundary condition: $f(0) = 0, f'(0) = 0, f'(infinty) = 1$

Solution:

Let $f1 = f, f2 = f'', f3 = f'''$

so that:

f1(i) = f1(i-1) + f2(i-1)*d_eta

f2(i) = f2(i-1) + f3(i-1)*d_eta

f3(i) = f3(i-1) - 0.5*f1(i-1)*f3(i-1)*d_eta

with bc f1(1) = 0, f2(1) = 0, but no f3(1), so we need to take a guess until this satisfies the bc f2(infinty) = 1;

That is the shooting method, we combine the Newton method to improve efficiency:

f3^{k+1}(1) = f3^{k}(1) - (f2^{k}(N) - 1)/(df2(N)/df3(1)) where k mean kth time of iteration

after dicresce it:

f3^{k+1}(1) = f3^{k}(1) - (f2^{k}(N) - 1) * (f3^{k}(1) - f3^{k-1}(1)) / (f2^{k}(N) - f2^{k-1}(N))

do the iteration until f2(N) - 1 < toleration

