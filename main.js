const questions = [
    {
        q: "Which header file is required for input and output operations in C++?",
        o: ["<stdio.h>", "<iostream>", "<conio.h>", "<stdlib.h>"],
        a: 1,
        topic: "Introduction & Syntax"
    },
    {
        q: "Which of the following is the correct syntax for the main function in C++?",
        o: ["void main()", "int main()", "main()", "both A and B"],
        a: 1,
        topic: "Introduction & Syntax"
    },
    {
        q: "C++ is an extension of which programming language?",
        o: ["Java", "Python", "C", "Basic"],
        a: 2,
        topic: "Introduction & Syntax"
    },
    {
        q: "Every statement in C++ must end with a:",
        o: ["Colon (:)", "Period (.)", "Semicolon (;)", "Comma (,)"],
        a: 2,
        topic: "Introduction & Syntax"
    },
    {
        q: "Which symbol is used for single-line comments in C++?",
        o: ["/* */", "#", "//", "!!"],
        a: 2,
        topic: "Introduction & Syntax"
    },
    {
        q: "Which data type is used to store decimal numbers in C++?",
        o: ["int", "char", "float", "bool"],
        a: 2,
        topic: "Data Types & Variables"
    },
    {
        q: "The size of an int data type is typically:",
        o: ["1 Byte", "2 Bytes", "4 Bytes", "8 Bytes"],
        a: 2,
        topic: "Data Types & Variables"
    },
    {
        q: "Which of the following is a valid variable name in C++?",
        o: ["2var", "_myVar", "my Var", "float"],
        a: 1,
        topic: "Data Types & Variables"
    },
    {
        q: "What is the correct way to declare a constant in C++?",
        o: ["const int x = 10;", "constant int x = 10;", "int const x : 10;", "#define x 10"],
        a: 0,
        topic: "Data Types & Variables"
    },
    {
        q: "Which data type is used to store high-precision floating-point numbers?",
        o: ["int", "float", "double", "long"],
        a: 2,
        topic: "Data Types & Variables"
    },
    {
        q: "Which operator is used for the modulus (remainder) operation?",
        o: ["/", "*", "%", "&"],
        a: 2,
        topic: "Operators"
    },
    {
        q: "Which of the following is a relational operator?",
        o: ["+", "==", "&&", "="],
        a: 1,
        topic: "Operators"
    },
    {
        q: "What is the result of 5 + 2 * 3 in C++?",
        o: ["21", "11", "10", "15"],
        a: 1,
        topic: "Operators"
    },
    {
        q: "The && operator stands for:",
        o: ["Logical OR", "Logical NOT", "Logical AND", "Assignment"],
        a: 2,
        topic: "Operators"
    },
    {
        q: "Which operator is used to increment a value by 1?",
        o: ["++", "--", "+=", "**"],
        a: 0,
        topic: "Operators"
    },
    {
        q: "Which statement is used to make a choice between two options?",
        o: ["for", "if-else", "switch", "while"],
        a: 1,
        topic: "Control Structures"
    },
    {
        q: "Which loop is guaranteed to execute at least once?",
        o: ["for", "while", "do-while", "none of the above"],
        a: 2,
        topic: "Control Structures"
    },
    {
        q: "The switch statement works with which data types?",
        o: ["float and double", "int and char", "string", "any data type"],
        a: 1,
        topic: "Control Structures"
    },
    {
        q: "What does the break statement do inside a loop?",
        o: ["Starts the next iteration", "Exits the loop immediately", "Pauses the program", "Restarts the loop"],
        a: 1,
        topic: "Control Structures"
    },
    {
        q: "Which of the following is the correct syntax for a for loop?",
        o: ["for (int i=0; i<10; i++)", "for (i=0; i<10)", "for (int i=0; i++)", "for (i<10; i++)"],
        a: 0,
        topic: "Control Structures"
    },
    {
        q: "A function that does not return any value has a return type of:",
        o: ["int", "null", "void", "empty"],
        a: 2,
        topic: "Functions"
    },
    {
        q: "The values passed to a function during a call are called:",
        o: ["Parameters", "Arguments", "Variables", "Inputs"],
        a: 1,
        topic: "Functions"
    },
    {
        q: "Which statement is used to send a value back from a function?",
        o: ["get", "send", "return", "exit"],
        a: 2,
        topic: "Functions"
    },
    {
        q: "Where is a function normally declared if it is used in main?",
        o: ["After main", "Inside main", "Before main", "In a separate file only"],
        a: 2,
        topic: "Functions"
    },
    {
        q: "Can multiple functions have the same name in C++ (Function Overloading)?",
        o: ["Yes, if parameters are different", "No, never", "Yes, if return types are different", "Only in classes"],
        a: 0,
        topic: "Functions"
    },
    {
        q: "What is the index of the first element in a C++ array?",
        o: ["1", "-1", "0", "User-defined"],
        a: 2,
        topic: "Arrays & Strings"
    },
    {
        q: "How do you declare an array of 5 integers?",
        o: ["int arr(5);", "int arr[5];", "arr int[5];", "int arr = {5};"],
        a: 1,
        topic: "Arrays & Strings"
    },
    {
        q: "In C++, std::string is part of which header?",
        o: ["<iostream>", "<string>", "<cstring>", "<stdlib.h>"],
        a: 1,
        topic: "Arrays & Strings"
    },
    {
        q: "What character marks the end of a C-style string?",
        o: ["\\n", "\\0", "\\t", ";"],
        a: 1,
        topic: "Arrays & Strings"
    },
    {
        q: "Which function is used to find the length of a std::string?",
        o: ["length()", "size()", "both A and B", "none of the above"],
        a: 2,
        topic: "Arrays & Strings"
    },
    {
        q: "What does a pointer variable store?",
        o: ["A value", "A memory address", "A character", "A boolean"],
        a: 1,
        topic: "Pointers & References"
    },
    {
        q: "Which operator is used to get the address of a variable?",
        o: ["*", "&", "->", "."],
        a: 1,
        topic: "Pointers & References"
    },
    {
        q: "The operator used to access the value at a memory address (dereferencing) is:",
        o: ["&", "*", "->", "++"],
        a: 1,
        topic: "Pointers & References"
    },
    {
        q: "What is a reference in C++?",
        o: ["A pointer to a pointer", "An alias for an existing variable", "A copy of a variable", "A constant pointer"],
        a: 1,
        topic: "Pointers & References"
    },
    {
        q: "What is the value of a null pointer?",
        o: ["1", "-1", "0 (or nullptr)", "Undefined"],
        a: 2,
        topic: "Pointers & References"
    },
    {
        q: "What is a class in C++?",
        o: ["A variable", "A function", "A blueprint for objects", "A data type for integers only"],
        a: 2,
        topic: "OOP Basics"
    },
    {
        q: "Which access specifier makes members accessible only within the class?",
        o: ["public", "protected", "private", "internal"],
        a: 2,
        topic: "OOP Basics"
    },
    {
        q: "The process of wrapping data and methods into a single unit is called:",
        o: ["Inheritance", "Polymorphism", "Encapsulation", "Abstraction"],
        a: 2,
        topic: "OOP Basics"
    },
    {
        q: "What is a constructor?",
        o: ["A function to delete objects", "A function to initialize objects", "A variable in a class", "A type of loop"],
        a: 1,
        topic: "OOP Basics"
    },
    {
        q: "Which operator is used to access members of a class using an object?",
        o: ["->", "::", ".", "&"],
        a: 2,
        topic: "OOP Basics"
    },
    {
        q: "Which namespace is cout part of?",
        o: ["std", "main", "io", "system"],
        a: 0,
        topic: "Standard Library"
    },
    {
        q: "What does cin stand for?",
        o: ["C Input", "Character Input", "Console Input", "Core Input"],
        a: 2,
        topic: "Standard Library"
    },
    {
        q: "Which manipulator is used to insert a newline and flush the buffer?",
        o: ["\\n", "endl", "newline", "flush"],
        a: 1,
        topic: "Standard Library"
    },
    {
        q: "Which header is needed to use the sqrt() function?",
        o: ["<iostream>", "<cmath>", "<maths>", "<stdlib.h>"],
        a: 1,
        topic: "Standard Library"
    },
    {
        q: "What is the purpose of using namespace std;?",
        o: ["To include all libraries", "To avoid using std:: prefix", "To speed up the program", "To create a new namespace"],
        a: 1,
        topic: "Standard Library"
    },
    {
        q: "Which of the following is the correct way to initialize a variable?",
        o: ["int x = 5;", "int x(5);", "int x{5};", "All of the above"],
        a: 3,
        topic: "Miscellaneous"
    },
    {
        q: "What is the size of a bool data type?",
        o: ["1 Byte", "4 Bytes", "1 bit", "8 Bytes"],
        a: 0,
        topic: "Miscellaneous"
    },
    {
        q: "Which keyword is used to handle exceptions in C++?",
        o: ["catch", "try", "throw", "All of the above"],
        a: 3,
        topic: "Miscellaneous"
    },
    {
        q: "What is the default return type of main()?",
        o: ["void", "int", "char", "float"],
        a: 1,
        topic: "Miscellaneous"
    },
    {
        q: "Which of the following is not a C++ keyword?",
        o: ["class", "volatile", "goto", "variable"],
        a: 3,
        topic: "Miscellaneous"
    },
    {
        q: "What is the output of cout << (10 > 5 && 5 > 10);?",
        o: ["1", "0", "true", "error"],
        a: 1,
        topic: "Logic & Loops"
    },
    {
        q: "A \"while\" loop check the condition:",
        o: ["Before the loop body", "After the loop body", "In the middle of the loop", "Never"],
        a: 0,
        topic: "Logic & Loops"
    },
    {
        q: "How do you write \"not equal to\" in C++?",
        o: ["<>", "!=", "~=", "!=="],
        a: 1,
        topic: "Logic & Loops"
    },
    {
        q: "What is the result of 10 / 3 in C++ if both are integers?",
        o: ["3.33", "3", "4", "Error"],
        a: 1,
        topic: "Logic & Loops"
    },
    {
        q: "Which keyword is used to skip the rest of the loop and start the next iteration?",
        o: ["break", "skip", "continue", "next"],
        a: 2,
        topic: "Logic & Loops"
    },
    {
        q: "What is the file extension for a C++ source file?",
        o: [".c", ".cpp", ".h", ".obj"],
        a: 1,
        topic: "Final Topics"
    },
    {
        q: "Can a C++ program run without a main function?",
        o: ["Yes", "No", "Only if it has classes", "Only in Linux"],
        a: 1,
        topic: "Final Topics"
    },
    {
        q: "Which of the following is used to group related constants?",
        o: ["struct", "enum", "union", "const array"],
        a: 1,
        topic: "Final Topics"
    },
    {
        q: "Which operator has the highest precedence?",
        o: ["+", "*", "()", "="],
        a: 2,
        topic: "Final Topics"
    },
    {
        q: "Who developed C++?",
        o: ["Dennis Ritchie", "Bjarne Stroustrup", "James Gosling", "Guido van Rossum"],
        a: 1,
        topic: "Final Topics"
    }
];

let currentIndex = 0;
let score = 0;
let startTime;
let timerInterval;
let canAnswer = true;

// UI Elements
const heroScreen = document.getElementById('hero-screen');
const quizScreen = document.getElementById('quiz-screen');
const resultScreen = document.getElementById('result-screen');

const questionText = document.getElementById('question-text');
const optionsGrid = document.getElementById('options-grid');
const currentQDisplay = document.getElementById('current-q');
const totalQsDisplay = document.getElementById('total-qs');
const liveScoreDisplay = document.getElementById('live-score');
const currentTopicDisplay = document.getElementById('current-topic');
const timerDisplay = document.getElementById('q-timer');
const progressIndicator = document.getElementById('progress-indicator');

const feedbackMessage = document.getElementById('feedback-message');
const nextBtn = document.getElementById('next-q-btn');

// Result elements
const finalScoreDisplay = document.getElementById('final-score');
const finalPercentDisplay = document.getElementById('final-percent');
const finalTimeDisplay = document.getElementById('final-time');
const rankNameDisplay = document.getElementById('rank-name');
const resultTagline = document.getElementById('result-tagline');

// Event Listeners
document.getElementById('start-quiz-btn').addEventListener('click', startQuiz);
document.getElementById('restart-btn').addEventListener('click', () => location.reload());

nextBtn.addEventListener('click', () => {
    currentIndex++;
    if (currentIndex < questions.length) {
        loadQuestion();
    } else {
        showResults();
    }
});

function startQuiz() {
    heroScreen.classList.add('hidden');
    quizScreen.classList.remove('hidden');
    totalQsDisplay.innerText = questions.length;
    startTime = new Date();
    startTimer();
    loadQuestion();
}

function loadQuestion() {
    canAnswer = true;
    nextBtn.classList.add('hidden');
    feedbackMessage.classList.add('hidden');

    const q = questions[currentIndex];
    questionText.innerText = q.q;
    currentQDisplay.innerText = currentIndex + 1;
    currentTopicDisplay.innerText = q.topic;

    // Update Progress
    const radius = 45;
    const circumference = 2 * Math.PI * radius;
    const offset = circumference - ((currentIndex + 1) / questions.length) * circumference;
    progressIndicator.style.strokeDashoffset = offset;

    optionsGrid.innerHTML = '';
    q.o.forEach((opt, idx) => {
        const btn = document.createElement('div');
        btn.className = 'option-card';
        btn.innerHTML = `<span class="opt-index">${String.fromCharCode(65 + idx)}</span> <span class="opt-text">${opt}</span>`;
        btn.onclick = () => handleAnswer(idx, btn);
        optionsGrid.appendChild(btn);
    });
}

function handleAnswer(idx, btn) {
    if (!canAnswer) return;
    canAnswer = false;

    const q = questions[currentIndex];
    const isCorrect = idx === q.a;

    if (isCorrect) {
        score++;
        btn.classList.add('correct');
        liveScoreDisplay.innerText = score;
        showFeedback("Correct! Excellent understanding.", true);
    } else {
        btn.classList.add('wrong');
        const options = optionsGrid.querySelectorAll('.option-card');
        options[q.a].classList.add('correct');
        showFeedback("Oops! That's not quite right.", false);
    }

    // Lock all options
    optionsGrid.querySelectorAll('.option-card').forEach(opt => opt.classList.add('locked'));
    nextBtn.classList.remove('hidden');
}

function showFeedback(msg, isSuccess) {
    feedbackMessage.innerText = msg;
    feedbackMessage.className = `feedback ${isSuccess ? 'success' : 'error'}`;
    feedbackMessage.classList.remove('hidden');
}

function startTimer() {
    timerInterval = setInterval(() => {
        const now = new Date();
        const diff = Math.floor((now - startTime) / 1000);
        const mins = Math.floor(diff / 60).toString().padStart(2, '0');
        const secs = (diff % 60).toString().padStart(2, '0');
        timerDisplay.innerText = `${mins}:${secs}`;
    }, 1000);
}

function showResults() {
    clearInterval(timerInterval);
    quizScreen.classList.add('hidden');
    resultScreen.classList.remove('hidden');

    const finalTime = timerDisplay.innerText;
    const percentage = Math.round((score / questions.length) * 100);

    finalScoreDisplay.innerText = score;
    finalPercentDisplay.innerText = `${percentage}%`;
    finalTimeDisplay.innerText = finalTime;

    // Rank & Tagline
    if (percentage === 100) {
        rankNameDisplay.innerText = "C++ Architect";
        resultTagline.innerText = "Flawless! You have mastered the C++ fundamentals.";
    } else if (percentage >= 90) {
        rankNameDisplay.innerText = "Modern Developer";
        resultTagline.innerText = "Exceptional performance! Your C++ skills are Sharp.";
    } else if (percentage >= 70) {
        rankNameDisplay.innerText = "Steady Coder";
        resultTagline.innerText = "Great job! A solid grasp of the core concepts.";
    } else if (percentage >= 50) {
        rankNameDisplay.innerText = "Aspiring Programmer";
        resultTagline.innerText = "Good effort! Keep practicing to strengthen your base.";
    } else {
        rankNameDisplay.innerText = "C++ Novice";
        resultTagline.innerText = "Every expert was once a beginner. Keep learning!";
    }
}
