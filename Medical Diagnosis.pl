% Facts: symptoms for diseases
disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(sore_throat),
    symptom(body_ache).

disease(cold) :-
    symptom(sneezing),
    symptom(runny_nose),
    symptom(sore_throat).

disease(covid19) :-
    symptom(fever),
    symptom(cough),
    symptom(loss_of_taste),
    symptom(breathing_difficulty).

disease(malaria) :-
    symptom(fever),
    symptom(chills),
    symptom(sweating),
    symptom(headache).

disease(typhoid) :-
    symptom(fever),
    symptom(abdominal_pain),
    symptom(weakness),
    symptom(loss_of_appetite).

% Ask user for symptoms dynamically
ask(Symptom) :-
    format('Do you have ~w? (yes/no): ', [Symptom]),
    read(Response),
    (Response == yes -> assertz(symptom(Symptom)) ; fail).

% Start diagnosis
diagnose :-
    retractall(symptom(_)),
    (
        disease(Disease),
        format('You may have ~w.', [Disease]), nl,
        fail
    ;
        \+ disease(_),
        write('No matching disease found.'), nl
    ).
