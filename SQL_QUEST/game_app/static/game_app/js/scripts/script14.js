document.getElementById("submit-query").addEventListener("click", function() {
    var sqlQuery = document.getElementById("sql-query").value.trim(); // Trim to remove leading and trailing whitespace

    // Check for specific SQL queries and display custom alert messages
    if (sqlQuery.toLowerCase().includes("delete")) {
        showAlert("Are you sure you want to delete data?"); // Alert message for delete query
        return;
    } else if (sqlQuery.toLowerCase().includes("update")) {
        showAlert("Are you sure you want to update data?"); // Alert message for update query
        return;
    } else if (sqlQuery.toLowerCase().includes("insert")) {
        showAlert("Are you sure you want to insert data?"); // Alert message for insert query
        return;
    } else if (sqlQuery.toLowerCase().includes("drop")) {
        showAlert("Are you sure you want to drop a table?"); // Alert message for drop query
        return;
    }

    // Modify SQL query to add prefix after "FROM"
    sqlQuery = addPrefixAfterFrom(sqlQuery, 'game_app_');

    // Log the modified SQL query to the console for verification
    console.log("Modified SQL Query:", sqlQuery);

    // Render the table based on the entered query
    renderTable(sqlQuery);

    // Expected correct query for passing the level
    var correctQuery = "SELECT virus_name FROM game_app_datafield WHERE virus_name='ILOVEYOU';";

    // Check if the user's query matches the correct query
     if (sqlQuery.toLowerCase() === correctQuery.toLowerCase()) {
        // Show success alert with green color
        showAlertSuccess("Congratulations! You passed the level.");

        // Disable the submit button temporarily
        document.getElementById("submit-query").disabled = true;

        // Redirect to the next page after 3 seconds
        setTimeout(function() {
            window.location.href = "/level15/";
        }, 3000);
    } else {
        showAlert("Not correct, try again..."); // Show alert if query does not match
    }
});

function addPrefixAfterFrom(sqlQuery, prefix) {
    // Use regular expression to find "FROM" followed by one or more spaces globally, then add the prefix
    return sqlQuery.replace(/FROM\s+/gi, "FROM " + prefix);
}
// Rest of the code remains unchanged...


function renderTable(sqlQuery) {
    // Send the SQL query to the server and retrieve the result
    executeQuery(sqlQuery, function(queryResult) {
        // Render the result in the dynamic table
        renderDynamicTable(queryResult);
    });
}

// Rest of the code remains unchanged...




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
    alertElement.className = "alert alert-danger";
    alertElement.textContent = message;

    // Append alert element to body
    document.body.appendChild(alertElement);

    // Remove alert after a certain time (e.g., 3 seconds)
    setTimeout(function() {
        document.body.removeChild(alertElement);
    }, 3000); // Adjust time as needed
}

function showAlertSuccess(message) {
    // Create alert element
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



function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
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



