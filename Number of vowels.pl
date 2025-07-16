% Define vowel characters
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% Base case: empty list has 0 vowels
count_vowels([], 0).

% Recursive case: head is a vowel
count_vowels([H|T], Count) :-
    vowel(H),
    count_vowels(T, Rest),
    Count is Rest + 1.

% Recursive case: head is not a vowel
count_vowels([H|T], Count) :-
    \+ vowel(H),
    count_vowels(T, Count).
