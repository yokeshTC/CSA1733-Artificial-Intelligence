% Graph structure: edge(Node, Neighbor, Cost)
edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 1).
edge(b, e, 5).
edge(c, f, 4).
edge(d, g, 2).
edge(f, g, 1).

% Heuristic function: h(Node, HeuristicValue)
h(a, 7).
h(b, 6).
h(c, 5).
h(d, 4).
h(e, 7).
h(f, 3).
h(g, 0).  % Goal node has heuristic 0

% Best-first search main entry
best_first(Start, Goal) :-
    best([[Start, 0]], Goal, []).

% Success case: Goal found
best([[Goal, _] | _], Goal, _) :-
    write('Goal reached: '), write(Goal), nl.

% Recursive case
best([[Current, _] | RestQueue], Goal, Visited) :-
    findall(
        [Next, H],
        (edge(Current, Next, _), \+ member(Next, Visited), h(Next, H)),
        Children
    ),
    append(RestQueue, Children, NewQueue),
    sort(2, @=<, NewQueue, SortedQueue),  % sort by heuristic (2nd element)
    write('Visiting: '), write(Current), nl,
    best(SortedQueue, Goal, [Current | Visited]).
