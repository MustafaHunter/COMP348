head([H|_], H).

tail([_|T], T).

cons([], List, List).
cons(List, [], List).
cons(ATOM, List2, [ATOM|List2]).
cons([H|T], List2, [H|T3]) :- cons(T, List2, T3).
