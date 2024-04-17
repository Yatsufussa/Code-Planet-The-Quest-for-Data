const dialogue = [
    "Scene: Nick approaches the infected lake, where he meets Iris, the lake's guardian.",
    "Nick: Hi, Iris. What happened to this lake?",
    "Iris: Hi, Nick. It's infected with a data virus. It's devouring our files!",
    "Nick: Just like in the Ash Lake Cavern in Dark Souls, where the hero may encounter dangers, this lake has fallen victim to a virus attack. I'll try to find a way to cleanse it.",
    "Iris: Be careful, the virus can be as aggressive as the Hydra lurking in the depths of the lake.",
    "Riddle: To progress further, determine the number of files in the database whose names start with the letter 'V'. Focus on this metric to find the virus trail. How many files is it?"
];


// Initialize dialogue index
let dialogueIndex = 0;
let currentTextIndex = 0;
let typingSpeed = 50; // Adjust typing speed in milliseconds (lower values for faster typing)

// Function to update dialogue content
let interval; // Declare interval outside the function scope

function updateDialogue() {
    clearInterval(interval); // Clear the interval before starting a new one

    const overlayContent = document.getElementById('overlay-content');
    const currentDialogue = dialogue[dialogueIndex];
    const character = currentDialogue.split(': ')[0];
    const dialogueText = currentDialogue.split(': ')[1] || currentDialogue; // Added to handle non-dialogue lines

    // Apply CSS class based on character
    if (character === "Nick") {
        overlayContent.innerHTML = `<span class="Nick">${character}: </span>`;
    } else if (character === "Iris") {
        overlayContent.innerHTML = `<span class="Iris">${character}: </span>`;
    } else {
        overlayContent.innerHTML = `<span>${character}: </span>`; // For non-dialogue lines
    }

    // Typing animation
    const textElement = overlayContent.querySelector('span');
    currentTextIndex = 0; // Reset currentTextIndex
    interval = setInterval(function() {
        textElement.textContent += dialogueText[currentTextIndex];
        currentTextIndex++;
        if (currentTextIndex === dialogueText.length) {
            clearInterval(interval);
        }
    }, typingSpeed);
}

// Add event listener to "Next" button
document.getElementById('next-button').addEventListener('click', function() {
    if (dialogueIndex < dialogue.length - 1) {
        dialogueIndex++;
        currentTextIndex = 0; // Reset current text index
        updateDialogue();
    }
});

// Add event listener to "Back" button
document.getElementById('back-button').addEventListener('click', function() {
    if (dialogueIndex > 0) {
        dialogueIndex--;
        currentTextIndex = 0; // Reset current text index
        updateDialogue();
    }
});

// Initial update of dialogue
updateDialogue();
