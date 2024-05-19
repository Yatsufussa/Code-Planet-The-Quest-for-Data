document.addEventListener("DOMContentLoaded", function() {
    // Define the click event listener for the Prev button
    document.getElementById("prevBtn").addEventListener("click", function() {
        toggleTables('current-table', 'ProcessingClouds');
    });

    // Define the click event listener for the Next button
    document.getElementById("nextBtn").addEventListener("click", function() {
        toggleTables('second-table', 'ProcessingClouds2');
    });

    // Define the function to toggle tables and update headings
    function toggleTables(tableId, headingText) {
        var currentTable = document.getElementById("current-table");
        var secondTable = document.getElementById("second-table");
        var currentTableHeading = document.getElementById("current-table-heading");
        var secondTableHeading = document.getElementById("second-table-heading");

        // Toggle table display based on the provided tableId
        if (tableId === 'current-table') {
            currentTable.style.display = "table";
            secondTable.style.display = "none";
            currentTableHeading.textContent = headingText;
            currentTableHeading.style.display = "block"; // Show current table heading
            secondTableHeading.style.display = "none"; // Hide second table heading
        } else {
            currentTable.style.display = "none";
            secondTable.style.display = "table";
            currentTableHeading.style.display = "none"; // Hide current table heading
            secondTableHeading.textContent = headingText; // Update and show second table heading
            secondTableHeading.style.display = "block";
        }
    }
});
