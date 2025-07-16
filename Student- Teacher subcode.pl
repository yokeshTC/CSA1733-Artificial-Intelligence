% Students
student(john).
student(sara).
student(ravi).
student(anu).

% Teachers
teacher(mr_smith).
teacher(ms_lee).

% Subject Codes
subject(cse101).
subject(cse102).

% Which teacher teaches which subject
teaches(mr_smith, cse101).
teaches(ms_lee, cse102).

% Which student is enrolled in which subject
enrolled(john, cse101).
enrolled(sara, cse102).
enrolled(ravi, cse101).
enrolled(anu, cse102).

% Rule: who teaches a student
teacher_of_student(Teacher, Student) :-
    enrolled(Student, Sub),
    teaches(Teacher, Sub).
