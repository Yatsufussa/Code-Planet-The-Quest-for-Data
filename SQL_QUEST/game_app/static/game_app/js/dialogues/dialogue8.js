const dialogue = [
    "Nick: I need information about the virus. Can you help?",
    "Archivist: Of course, my young friend. But information about the virus is very valuable.",
    "Nick: I'm willing to pay any price to save the planet.",
    "Archivist: In that case, let's begin the search.",
    "Riddle: There is a log of virus-related events in the database. Which table contains this log?"
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
    const dialogueText = currentDialogue.split(': ')[1];

    // Apply CSS class based on character
    if (character.includes('Nick')) {
        overlayContent.innerHTML = `<span class="Nick">${character}: </span>`;
    } else if (character.includes('Archivist')) {
        overlayContent.innerHTML = `<span class="Archivist">${character}: </span>`;
    } else if (character.includes('Riddle')) {
        overlayContent.innerHTML = `<span class="Riddle">${character}: </span>`;
    }

    // Typing animation
    const textElement = overlayContent.querySelector('span');
    let currentTextIndex = 0; // Reset currentTextIndex
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
