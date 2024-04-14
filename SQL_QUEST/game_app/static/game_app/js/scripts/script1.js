document.getElementById("submit-query").addEventListener("click", function() {
    var sqlQuery = document.getElementById("sql-query").value.trim(); // Trim to remove leading and trailing whitespace

    // Validate SQL query
    if (sqlQuery === "") {
        showAlert("Please enter a valid SQL query."); // Show alert if SQL query is empty
        return; // Exit function if SQL query is empty
    }

    console.log("SQL Query:", sqlQuery); // Log the SQL query value

    // Normalize the SQL query and correct answer for comparison
    var normalizedSqlQuery = normalizeSqlQuery(sqlQuery);
    var normalizedCorrectQuery = normalizeSqlQuery("SELECT virus_name FROM game_app_datafield WHERE virus_name='ILOVEYOU';");

    // Check for specific SQL queries and display custom alert messages
    if (normalizedSqlQuery.includes("delete")) {
        showAlert("Are you sure you want to delete data?"); // Alert message for delete query
    } else if (normalizedSqlQuery.includes("update")) {
        showAlert("Are you sure you want to update data?"); // Alert message for update query
    } else if (normalizedSqlQuery.includes("insert")) {
        showAlert("Are you sure you want to insert data?"); // Alert message for insert query
    } else if (normalizedSqlQuery.includes("drop")) {
        showAlert("Are you sure you want to drop data?"); // Alert message for insert query
    } else {
        // Send the SQL query to the server and retrieve the result
        executeQuery(sqlQuery, function(queryResult) {
            // Render the result in the dynamic table
            renderDynamicTable(queryResult);

            // Check if the SQL query matches the correct answer exactly
            if (normalizedSqlQuery === normalizedCorrectQuery) {
                showAlert("Correct!"); // Alert message for correct query
                // Redirect to the next HTML page after 3 seconds
                setTimeout(function() {
                    window.location.href = "/start_game/level_2/"; // Change the URL as needed
                }, 3000);
            } else {
                showAlert("Incorrect, try again."); // Alert message for incorrect query
            }
        });
    }
});



function normalizeSqlQuery(sqlQuery) {
    // Trim leading and trailing whitespace
    var normalizedQuery = sqlQuery.trim();
    // Replace single quotes with double quotes
    normalizedQuery = normalizedQuery.replace(/'/g, '"');
    // Remove excess spaces around equals sign
    normalizedQuery = normalizedQuery.replace(/\s*=\s*/g, '=');

    // Check if the query contains the app name as a prefix and remove it
    normalizedQuery = removeAppPrefix(normalizedQuery);

    return normalizedQuery.toLowerCase(); // Return the normalized query
}

function removeAppPrefix(query) {
    // Define your app name here
    var appName = "game_app";

    // Check if the query starts with the app name followed by a dot and remove it
    if (query.toLowerCase().startsWith(appName.toLowerCase() + '.')) {
        return query.substring(appName.length + 1); // Add 1 to also remove the dot
    }
    return query;
}




function renderTable(sqlQuery) {
    // Send the SQL query to the server and retrieve the result
    executeQuery(sqlQuery, function(queryResult) {
        // Render the result in the dynamic table
        renderDynamicTable(queryResult);
    });
}

function showAlert(message) {
    // Create alert element
    var alertElement = document.createElement("div");
    alertElement.className = "alert";
    alertElement.textContent = message;

    // Append alert element to body
    document.body.appendChild(alertElement);

    // Remove alert after a certain time (e.g., 3 seconds)
    setTimeout(function() {
        document.body.removeChild(alertElement);
    }, 3000); // Adjust time as needed
}

function showSuccessAlert(message) {
    // Create alert element with success class
    var alertElement = document.createElement("div");
    alertElement.className = "alert alert-success";
    alertElement.textContent = message;

    // Append alert element to body
    document.body.appendChild(alertElement);

    // Remove alert after a certain time (e.g., 3 seconds)
    setTimeout(function() {
        document.body.removeChild(alertElement);
    }, 3000); // Adjust time as needed
}

function openNewWindow() {
    // Open a new window or tab after successful execution
    var newWindow = window.open("level_2.html", "_blank");
    // You can customize the URL and window properties as needed.
}

function executeQuery(sqlQuery, callback) {
    console.log("SQL Query:", sqlQuery);
    var csrftoken = getCookie('csrftoken'); // Function to retrieve CSRF token from cookies

    fetch('/execute_query/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  // Include CSRF token in headers
        },
        body: JSON.stringify({ sqlQuery: sqlQuery })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        callback(data);
    })
    .catch(error => console.error('Error:', error));
}

function renderDynamicTable(queryResult) {
    var dynamicTable = document.getElementById("dynamic-table");
    dynamicTable.innerHTML = ""; // Clear previous content

    // Create the table structure
    var table = document.createElement("table");
    var thead = document.createElement("thead");
    var tbody = document.createElement("tbody");
    var trHead = document.createElement("tr");

    // Add table headers
    Object.keys(queryResult[0]).forEach(function(key) {
        var th = document.createElement("th");
        th.textContent = key;
        trHead.appendChild(th);
    });
    thead.appendChild(trHead);
    table.appendChild(thead);

    // Add table rows
    queryResult.forEach(function(rowData) {
        var tr = document.createElement("tr");
        Object.values(rowData).forEach(function(value) {
            var td = document.createElement("td");
            td.textContent = value;
            tr.appendChild(td);
        });
        tbody.appendChild(tr);
    });
    table.appendChild(tbody);

    dynamicTable.appendChild(table);
}
