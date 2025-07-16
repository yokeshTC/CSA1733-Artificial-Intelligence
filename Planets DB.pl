% planet(Name, DistanceFromSun in million km, Diameter in km, NumberOfMoons, Type).

planet(mercury, 57.9, 4879, 0, terrestrial).
planet(venus, 108.2, 12104, 0, terrestrial).
planet(earth, 149.6, 12742, 1, terrestrial).
planet(mars, 227.9, 6779, 2, terrestrial).
planet(jupiter, 778.3, 139820, 79, gas_giant).
planet(saturn, 1427, 116460, 82, gas_giant).
planet(uranus, 2871, 50724, 27, ice_giant).
planet(neptune, 4497.1, 49244, 14, ice_giant).

% Rule: Find planets by type
planet_type(Type, Name) :-
    planet(Name, _, _, _, Type).

% Rule: Find planets with more than N moons
planet_with_more_moons(N, Name) :-
    planet(Name, _, _, Moons, _),
    Moons > N.

% Rule: Get closest planet to sun
closest_planet(Name) :-
    planet(Name, Distance, _, _, _),
    \+ (planet(_, D2, _, _, _), D2 < Distance).
