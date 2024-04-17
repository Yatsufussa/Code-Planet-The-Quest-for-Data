const dialogue = [
    "Scene: Nick reaches the data management center, where the main source of the virus is located. He is ready to fight it in the final battle.",
    "Nick: This is where it all began...",
    "Nick prepares for the final showdown with the main source of the virus",
    "Riddle: To add data to a table in SQL, a specific keyword is used. What keyword is it?"
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
    } else if (character === "Sam") {
        overlayContent.innerHTML = `<span class="Sam">${character}: </span>`;
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
