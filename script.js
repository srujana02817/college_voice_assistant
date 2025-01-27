// Initialize Speech Recognition and Speech Synthesis
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
const synth = window.speechSynthesis;

// DOM Elements
const startButton = document.getElementById("start-btn");
const submitButton = document.getElementById("submit-btn");
const textInput = document.getElementById("text-input");
const outputBox = document.getElementById("output-box");

// Speech Recognition Configuration
recognition.lang = "en-US";
recognition.interimResults = false;

let isListening = false;

// Event Listeners

// Start Listening Button
startButton.addEventListener("click", () => {
    isListening = !isListening;

    if (isListening) {
        startButton.textContent = 'Stop Listening';
        startButton.classList.add('active');
        outputBox.innerHTML = "Listening... Please speak.";
        recognition.start();  // Start speech recognition
    } else {
        startButton.textContent = 'Start Listening';
        startButton.classList.remove('active');
        recognition.stop();  // Stop speech recognition
        outputBox.innerHTML += "<br>Stopped listening.";
    }
});

// Result from Speech Recognition
recognition.addEventListener("result", (event) => {
    const command = event.results[0][0].transcript;
    handleCommand(command);
});

// Handle Send Button
submitButton.addEventListener("click", () => {
    const command = textInput.value.trim();
    if (command) {
        handleCommand(command);
        textInput.value = "";  // Clear input field
    } else {
        outputBox.innerHTML = "Please enter a command.";
    }
});

// Handle Commands (Text and Speech)
function handleCommand(command) {
    outputBox.innerHTML = `You said: "${command}"`;
    const response = interpretCommand(command);
    outputBox.innerHTML += `<br>Assistant: ${response}`;
    speakText(response);
}

// Speak Text Function
function speakText(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    synth.speak(utterance);
}

// Interpret Command Function
function interpretCommand(command) {
    const lowerCommand = command.toLowerCase();

    // Common greetings
    if (lowerCommand.includes("hi") || lowerCommand.includes("hello")) {
        return "Hello! How can I assist you today?";
    }

    // Asking for the time
    if (lowerCommand.includes("time")) {
        const currentTime = new Date().toLocaleTimeString();
        return `The current time is ${currentTime}.`;
    }

    // Asking for the date
    if (lowerCommand.includes("date")) {
        const currentDate = new Date().toLocaleDateString();
        return `Today's date is ${currentDate}.`;
    }

    // Fallback for unrecognized commands
    return "I'm not sure I understand that. Could you please rephrase?";
}

// Handle Errors
recognition.addEventListener("error", (event) => {
    outputBox.innerHTML = `Error: ${event.error}`;
});

recognition.addEventListener("end", () => {
    outputBox.innerHTML += "<br>Stopped listening. Click 'Start Listening' to try again.";
});
