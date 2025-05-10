:- consult('solar.pl').

planet(X) :- mass(X, Y), Y > 0.33, orbits(X, sun).

is_satellite_of(X, Y) :- orbits(X, Y), planet(Y).

obtain_all_satellites(X, L) :- findall(Y, is_satellite_of(Y, X), L).
