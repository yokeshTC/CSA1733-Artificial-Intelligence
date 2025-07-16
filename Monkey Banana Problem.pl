% state(MonkeyLocation, BoxLocation, MonkeyStatus, HasBanana)

% Goal state: monkey has the banana
goal(state(_, _, _, has)).

% Possible actions:

% 1. Monkey walks from one place to another
move(state(Monkey, Box, onfloor, no),
     walk(Monkey, NewPos),
     state(NewPos, Box, onfloor, no)) :-
    Monkey \= NewPos.

% 2. Monkey pushes the box from one place to another
move(state(Monkey, Monkey, onfloor, no),
     push(Monkey, NewPos),
     state(NewPos, NewPos, onfloor, no)) :-
    Monkey \= NewPos.

% 3. Monkey climbs on the box
move(state(Pos, Pos, onfloor, no),
     climb,
     state(Pos, Pos, onbox, no)).

% 4. Monkey grabs the banana
move(state(Pos, Pos, onbox, no),
     grab,
     state(Pos, Pos, onbox, has)).

% Plan: find a sequence of moves to reach goal
plan(State, [], State) :-
    goal(State).

plan(State1, [Move | Moves], FinalState) :-
    move(State1, Move, State2),
    plan(State2, Moves, FinalState).

% Start planning from initial state
solve :-
    plan(state(atdoor, atwindow, onfloor, no), Moves, _),
    write('Plan to get the banana:'), nl,
    write_steps(Moves).

write_steps([]).
write_steps([Step | Rest]) :-
    write('- '), write(Step), nl,
    write_steps(Rest).
