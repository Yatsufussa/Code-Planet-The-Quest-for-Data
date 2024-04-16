const dialogue = [
    "Nick: Hello, Algorithm. I need a path through these mountains.",
    "Algorithm: Hello, Nick. I see you're seeking answers.",
    "Nick: Yes, I need to find the key to fighting the virus.",
    "Algorithm: May the algorithms be on your side.",
    "Riddle: \"To continue your journey and search for the key to fighting the virus, consider which search algorithm is most efficient for sorting large volumes of data. This algorithm has a complexity of O(n log n) and is widely used in the field of information technology. What algorithm is it?\""
    // Add more dialogues as needed
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
    } else if (character.includes('Algorithm')) {
        overlayContent.innerHTML = `<span class="Algorithm">${character}: </span>`;
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
