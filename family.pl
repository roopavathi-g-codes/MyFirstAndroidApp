% -------- FACTS --------

parent(john, mary).
parent(john, sam).
parent(mary, anna).
parent(mary, tom).

male(john).
male(sam).
male(tom).

female(mary).
female(anna).

% -------- RULES --------

% Father rule
father(X, Y) :-
    parent(X, Y),
    male(X).

% Mother rule
mother(X, Y) :-
    parent(X, Y),
    female(X).

% Grandparent rule
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Sibling rule
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.