const dialogue = [
    "Scene: Nick descends into the depths of the databases, where the darkest corner, inhabited by the virus, lies.",
    "Nick: It's so dark and gloomy here...",
    "Nick delves into the deepest levels of the databases, battling the virus",
    "Riddle: To compare values in SQL, a specific operator is used. What operator is it?"
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
