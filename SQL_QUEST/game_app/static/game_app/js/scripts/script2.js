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
var level_id = 2;

async function getPlayerId() {
    try {
        const response = await fetch('/get_player_id/');
        const data = await response.json();
        return data.player_id;
    } catch (error) {
        console.error('Error fetching player ID:', error);
        return null;
    }
}

document.addEventListener("DOMContentLoaded", async function() {
    playerId = await getPlayerId();
    startTimer();
});

document.getElementById("submit-query").addEventListener("click", async function() {
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

    var correctQuery = "SELECT SUM(NumberOfAbsorbedFiles) AS answer FROM game_app_LakeData WHERE LakeDatabase IN ('BeautifulDb', 'PureH2ODB');";

    if (sqlQuery.toLowerCase() === correctQuery.toLowerCase()) {
        showAlertSuccess("Congratulations! You passed the level.");
        var elapsedTime = (new Date().getTime() - startTime) / 1000;
        await recordLevelCompletion(playerId, elapsedTime);

        document.getElementById("submit-query").disabled = true;
        setTimeout(function() {
            window.location.href = "/level3/";
        }, 3000);
    } else {
        showAlert("Not correct, try again...");
    }
});

async function recordLevelCompletion(playerId, elapsedTime) {
    try {
        const response = await fetch('/record_level_completion/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                'player_id': playerId,
                'level_id': 2,
                'elapsed_time': elapsedTime,
                'retry_count': retryCount
            })
        });

        if (response.ok) {
            console.log("Level completion recorded successfully.");
        } else {
            const data = await response.json();
            console.error("Failed to record level completion:", data.error);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function addPrefixAfterFrom(sqlQuery, prefix) {
    return sqlQuery.replace(/FROM\s+/gi, "FROM " + prefix);
}

function renderTable(sqlQuery) {
    executeQuery(sqlQuery, renderDynamicTable);
}

function showAlert(message) {
    createAlert("alert alert-danger", message);
}

function showAlertSuccess(message) {
    createAlert("alert alert-success", message);
}

function createAlert(className, message) {
    var alertElement = document.createElement("div");
    alertElement.className = className;
    alertElement.textContent = message;
    document.body.appendChild(alertElement);
    setTimeout(function() {
        document.body.removeChild(alertElement);
    }, 3000);
}

function executeQuery(sqlQuery, callback) {
    console.log("SQL Query:", sqlQuery);
    fetch('/execute_query/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ sqlQuery: sqlQuery })
    })
    .then(response => response.json())
    .then(data => callback(data))
    .catch(error => console.error('Error:', error));
}

function renderDynamicTable(queryResult) {
    var dynamicTable = document.getElementById("dynamic-table");
    dynamicTable.innerHTML = "";
    var table = document.createElement("table");
    var thead = document.createElement("thead");
    var tbody = document.createElement("tbody");
    var trHead = document.createElement("tr");

    Object.keys(queryResult[0]).forEach(key => {
        var th = document.createElement("th");
        th.textContent = key;
        trHead.appendChild(th);
    });
    thead.appendChild(trHead);
    table.appendChild(thead);

    queryResult.forEach(rowData => {
        var tr = document.createElement("tr");
        Object.values(rowData).forEach(value => {
            var td = document.createElement("td");
            td.textContent = value;
            tr.appendChild(td);
        });
        tbody.appendChild(tr);
    });
    table.appendChild(tbody);
    dynamicTable.appendChild(table);
}