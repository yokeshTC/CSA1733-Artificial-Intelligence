% match(Pattern, List): true if Pattern matches the beginning of List

match([], []).
match([any|PTail], [_|LTail]) :-
    match(PTail, LTail).
match([X|PTail], [X|LTail]) :-
    match(PTail, LTail).

% match_anywhere(Pattern, List): true if Pattern matches any sublist of List

match_anywhere(Pattern, List) :-
    append(_, rest, List),
    append(Pattern, _, rest),
    match(Pattern, rest).
