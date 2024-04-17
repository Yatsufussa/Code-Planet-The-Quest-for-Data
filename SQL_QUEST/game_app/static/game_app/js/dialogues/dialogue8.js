const dialogue = [
    "Scene: Nick enters the valley where database indexes are stored. He meets the indexer who will help him find the keys to the databases.",
    "Nick: Hello, I'm looking for keys to the databases to find their vulnerabilities.",
    "Indexer: Hello, Nick. I can help you find the necessary indexes.",
    "Nick: I need to find an entry point to fight the virus.",
    "Indexer: We can start by analyzing the indexes of the databases.",
    "Riddle: To find the path to accelerating data retrieval, focus on the type of index most commonly used for this purpose. This type of index is considered the most efficient and widely used in the world of databases. What type of index is it?"
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
    } else if (character === "Indexer") {
        overlayContent.innerHTML = `<span class="Indexer">${character}: </span>`;
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
