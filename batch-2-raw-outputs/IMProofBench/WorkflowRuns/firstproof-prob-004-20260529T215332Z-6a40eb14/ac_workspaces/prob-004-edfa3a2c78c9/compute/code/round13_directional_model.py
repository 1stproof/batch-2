from itertools import combinations

pairs = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]

# Source directional filling weights after converting projected slice volumes
# to complementary minors of the slicing map F=(f_a,f_b):
# q=(i,j) labels the source minor d(f_a,f_b)/d(x_i,x_j).
weights_name = {
    (1,2): 'R1', (1,3): 'R1', (1,4): 'R1',
    (2,3): 'R2', (2,4): 'R2',
    (3,4): 'R3',
}

# Stress family from the notes.
s = {1:0, 2:0, 3:6, 4:6}       # S=(1,1,L^6,L^6)
r = {1:-1, 2:4, 3:5, 4:6}      # R=(L^-1,L^4,L^5,L^6)
w_exp = {(1,2):r[1], (1,3):r[1], (1,4):r[1],
         (2,3):r[2], (2,4):r[2], (3,4):r[3]}
V_exp = sum(r.values())
Svol_exp = sum(s.values())
desired_exp = s[1] + 0.5*s[2] + 1.5*s[3] + s[4]
first_alt_exp_R = r[3] + r[4]
first_alt_exp_S = s[3] + s[4]

# Diagonal derivative exponent model A=diag(L^a_i).  This is not claimed to be
# a rectangle map; it is a pointwise Lambda^2 df/degree algebra model.
a = {1:0, 2:-1, 3:-1, 4:0}
B_exp = {p: a[p[0]] + a[p[1]] for p in pairs}
det_exp = sum(a.values())
max_pair_exp = max(B_exp.values())

def lhs_exp(target_pair):
    return Svol_exp + min(s[target_pair[0]], s[target_pair[1]])

def rhs_terms_for_row(target_pair):
    out = []
    for q in pairs:
        # diagonal compound matrix: row target_pair has only column target_pair nonzero
        if q == target_pair:
            out.append((q, V_exp + B_exp[q] + w_exp[q]))
    return out

print('pairs:', pairs)
print('source minor weights w_q:', weights_name)
print('S exponents:', [s[i] for i in range(1,5)])
print('R exponents:', [r[i] for i in range(1,5)], 'Vol(R) exponent', V_exp)
print('Vol(S) exponent:', Svol_exp)
print('desired exponent S1*S2^(1/2)*S3^(3/2)*S4:', desired_exp)
print('first alternative exponents R3R4 vs S3S4:', first_alt_exp_R, first_alt_exp_S)
print('diagonal A exponents:', [a[i] for i in range(1,5)])
print('Lambda^2 diagonal exponents:', {str(k):v for k,v in B_exp.items()})
print('max pair exponent (Dil_2<=1 iff <=0):', max_pair_exp)
print('det exponent; degree integral exponent Vol(R)+det:', det_exp, V_exp + det_exp)
print('compound Plucker/conformal relation check:')
print('  for A=diag(L^a_i), B^T J B = L^det(A) J because')
print('  B12*B34, -B13*B24, B14*B23 exponents are:',
      B_exp[(1,2)] + B_exp[(3,4)],
      B_exp[(1,3)] + B_exp[(2,4)],
      B_exp[(1,4)] + B_exp[(2,3)])
print('\nDirectional inequalities, exponents of L:')
print('target_pair  LHS=S_a*Vol(S)  available_RHS_term  slack')
for A in pairs:
    L = lhs_exp(A)
    terms = rhs_terms_for_row(A)
    best = max(e for _, e in terms) if terms else float('-inf')
    print(f'{A!s:>10}  {L:>6}              {terms!s:>18}  {best-L:>5}')
