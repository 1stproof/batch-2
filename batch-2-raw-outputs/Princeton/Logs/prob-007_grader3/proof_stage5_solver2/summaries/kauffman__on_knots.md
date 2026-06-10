<!-- Generated 2026-05-31T03:11:38 -->
<!-- Source PDF: kauffman__on_knots.pdf (1042195 bytes) -->
<!-- Citation: Louis H. Kauffman (1987). On Knots. Princeton University Press. -->

# On Knots (Louis H. Kauffman, 1987)

## Definitions
- **Definition [Flag: missing label].** We shall say that ZG is an invariant of finite type i if ZG vanishes for all graphs with greater than i nodes.
- **Definition [Flag: missing label].** A Lie algebra is a vector space L over a field F that is closed under a binary operation, called the Lie bracket and denoted by [B,C] for B and C in L. The bracket is assumed to satisfy the following axioms.
1. [X,Y] = -[Y,X] for all X and Y in L.
2. [aX+bY,Z] = a[X,Z] + b[Y,Z] for all a and b in F and X,Y,Z in L.
3. [X,[Y,Z]] + [Z,[X,Y]] + [Y,[Z,X]] = 0.

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem [Flag: missing label].** Every diagram that is obtained from the standard trefoil diagram by Reidemeister moves can be 3-colored. Hence the trefoil diagram represents a knot.
  *Proof:* Demonstrates visually that any Reidemeister move preserves the possibility of exactly 3-coloring the diagram.

- **Lemma [Flag: missing label].** Let K be a given link diagram, and let K denote a diagram that is obtained from K by performing a type 2 Reidemeister move in the simplifying direction (eliminating two crossings from K). Let K be the diagram obtained from K by replacing the site of the type two move by two arcs in the opposite pattern to the form of the simplified site in K. (The diagrams in Figure 28 illustrate this construction.) Then
<K> = AB<K> + (ABd + A 2 + B2)<K>.
  *Proof:* Expands the bracket polynomial across the four local states of a Type II move site and groups the resulting coefficients.

- **Lemma [Flag: missing label].** Let <K> denote the bracket state sum with B=A-1 and
d=-A2-A-2. Then <K> is invariant under the Reidemeister moves II and III and on move I behaves as shown below.
                                < K(+) > = (-A3)< K >
                                < K(-) > = (-A-3)< K >.
  *Proof:* Extends the previously established invariance under Type II and III moves to Type I moves by direct substitution into the bracket equations.

- **Lemma [Flag: missing label].** If ZG is a Vassiliev invariant of finite type i, then ZG is independent of the embedding of the graph G when G has i vertices.
  *Proof:* Evaluates a crossing switch as the difference between the graph and a graph with an additional node, which vanishes by the finite-type assumption.

- **Theorem [Flag: missing label].** Let VG(t) denote the Jones polynomial extended to rigid
vertex 4-valent graphs by the formula VK+ - VK- = VK# .
Let vi(G) denote the coefficient of xi in the expansion of VG(exp(x)). Then vi(G) is a Vassiliev invariant of type i.
  *Proof:* Substitutes $t = \exp(x)$ into the oriented state expansion formula, showing the resulting difference across a singular crossing is divisible by $x$.