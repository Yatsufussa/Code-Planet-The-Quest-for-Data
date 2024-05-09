 document.addEventListener("DOMContentLoaded", function() {
            // Your JavaScript code here
            document.getElementById("prevBtn").addEventListener("click", function() {
                toggleTables('current-table', 'Index_Valley');
            });

            document.getElementById("nextBtn").addEventListener("click", function() {
                toggleTables('second-table', 'Index_Valley2');
            });

            function toggleTables(tableId, headingText) {
                console.log("Toggle tables called with tableId:", tableId);
                var currentTable = document.getElementById("current-table");
                var secondTable = document.getElementById("second-table");
                var currentTableHeading = document.querySelector("#current-table .table-heading");
                var secondTableHeading = document.querySelector("#second-table .table-heading");

                if (tableId === 'current-table') {
                    currentTable.style.display = "table";
                    secondTable.style.display = "none";
                    currentTableHeading.textContent = headingText;
                    secondTableHeading.textContent = ""; // Clear second table heading
                } else {
                    currentTable.style.display = "none";
                    secondTable.style.display = "table";
                    currentTableHeading.textContent = ""; // Clear current table heading
                    secondTableHeading.textContent = headingText; // Update second table heading
                }
            }
        });