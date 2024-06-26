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

var retryCount = 0;
var csrftoken = getCookie('csrftoken');
var playerId;

getPlayerId().then(id => {
    playerId = id;
}).catch(error => {
    console.error('Error fetching player ID:', error);
});

function getPlayerId() {
    return fetch('/get_player_id/')
        .then(response => response.json())
        .then(data => data.player_id)
        .catch(error => {
            console.error('Error fetching player ID:', error);
            return null;
        });
}

document.getElementById("submit-query").addEventListener("click", function() {
    retryCount++;
    var sqlQuery = document.getElementById("sql-query").value.trim();

    if (sqlQuery.toLowerCase().includes("delete") ||
        sqlQuery.toLowerCase().includes("update") ||
        sqlQuery.toLowerCase().includes("insert") ||
        sqlQuery.toLowerCase().includes("drop")) {
        showAlert("Are you sure you want to perform this operation?");
        return;
    }

    sqlQuery = addPrefixAfterFrom(sqlQuery, 'game_app_');
    console.log("Modified SQL Query:", sqlQuery);

    renderTable(sqlQuery);

    var correctQuery = "SELECT virusname FROM game_app_datafield WHERE virusname='ILOVEYOU';";
    if (sqlQuery.toLowerCase() === correctQuery.toLowerCase()) {
        showAlertSuccess("Congratulations! You passed the level.");
        var elapsedTime = (new Date().getTime() - startTime) / 1000;
        recordLevelCompletion(playerId, elapsedTime);

        document.getElementById("submit-query").disabled = true;
        setTimeout(function() {
            window.location.href = "/level2/";
        }, 3000);
    } else {
        showAlert("Not correct, try again...");
    }
});
document.getElementById("hint-button").addEventListener("click", function() {
    fetchHint().then(hint => {
        var hintContainer = document.getElementById("hint-container");
        var hintContent = document.getElementById("hint-content");
        hintContent.textContent = hint;
        hintContainer.style.display = "block";

        // Hide the hint after 10 seconds (10000 milliseconds)
        setTimeout(function() {
            hintContainer.style.display = "none";
        }, 10000);
    }).catch(error => {
        console.error('Error fetching hint:', error);
        showAlert("Could not fetch hint. Please try again later.");
    });
});

function fetchHint() {
    return fetch('/get_hint/?level_id=1')
        .then(response => response.json())
        .then(data => data.hint)
        .catch(error => {
            console.error('Error fetching hint:', error);
            return "No hint available.";
        });
}

function recordLevelCompletion(playerId, elapsedTime) {
    fetch('/record_level_completion/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'player_id': playerId,
            'level_id': 1,
            'elapsed_time': elapsedTime,
            'retry_count': retryCount
        })
    })
    .then(response => {
        if (response.ok) {
            console.log("Level completion recorded successfully.");
        } else {
            response.json().then(data => {
                console.error("Failed to record level completion:", data.error);
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

window.onload = function() {
    // Display the hidden treasure after a delay or specific action
    setTimeout(function() {
        document.getElementById("hidden-treasure").style.display = "block";
    }, 5000); // Display after 5 seconds (adjust as needed)
};

function addPrefixAfterFrom(sqlQuery, prefix) {
    return sqlQuery.replace(/FROM\s+/gi, "FROM " + prefix);
}

function renderTable(sqlQuery) {
    executeQuery(sqlQuery, function(queryResult) {
        renderDynamicTable(queryResult);
    });
}

function showAlert(message) {
    var alertElement = document.createElement("div");
    alertElement.className = "alert alert-danger";
    alertElement.textContent = message;
    document.body.appendChild(alertElement);
    setTimeout(function() {
        document.body.removeChild(alertElement);
    }, 3000);
}

function showAlertSuccess(message) {
    var alertElement = document.createElement("div");
    alertElement.className = "alert alert-success";
    alertElement.textContent = message;
    document.body.appendChild(alertElement);
    setTimeout(function() {
        document.body.removeChild(alertElement);
    }, 3000);
}

function executeQuery(sqlQuery, callback) {
    console.log("SQL Query:", sqlQuery);
    var csrftoken = getCookie('csrftoken');

    fetch('/execute_query/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
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
    dynamicTable.innerHTML = "";

    var table = document.createElement("table");
    var thead = document.createElement("thead");
    var tbody = document.createElement("tbody");
    var trHead = document.createElement("tr");

    Object.keys(queryResult[0]).forEach(function(key) {
        var th = document.createElement("th");
        th.textContent = key;
        trHead.appendChild(th);
    });
    thead.appendChild(trHead);
    table.appendChild(thead);

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

document.getElementById("hidden-treasure").addEventListener("click", function() {
    // Disable the button to prevent multiple clicks
    this.disabled = true;

    fetch('/increment_player_level/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ player_id: playerId })
    })
    .then(response => {
        if (response.ok) {
            alert("Treasure found! Player level increased.");
            // Hide the button after a successful response
            this.style.display = "none";
        } else {
            response.json().then(data => {
                alert("Error: " + data.error);
                // Re-enable the button if there was an error
                this.disabled = false;
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
        // Re-enable the button if there was an error
        this.disabled = false;
    });
});

