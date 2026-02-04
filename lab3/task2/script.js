

class HTTPWrapper {

    constructor() {
        this.url = "http://127.0.0.1:8000/tasks";
    }

    async request(method, path, headers, data) {
        const settings = {};

        settings['method'] = method;
        if (headers) settings['headers'] = headers;
        if (data) settings['body'] = JSON.stringify(data);

        let response;

        try {
            response = await fetch(this.url + path, settings);
            return response;
        }
        catch (err) {
            alert("fetch() error : " + err);
            return response;
        }
    }

    async getExistingTasks() {
        const response = await this.request("GET", "/get-task-list", null, null);
        if (!response.ok) {
            alert("GET error : " + response.status);
        }
        return response;
    }

    async postTask(taskName) {
        const data = { "task_name": taskName };
        const response = await this.request("POST", "/create-task", { "Content-Type": "application/json" }, data);
        if (!response.ok) {
            alert("POST error : " + response.status);
        }
        return response;
    }

    async deleteTask(taskName) {
        const data = { "task_name": taskName };
        const response = await this.request("DELETE", "/delete-task", { "Content-Type": "application/json" }, data);
        if (!response.ok) {
            alert("DELETE error : " + response.status);
        }
        return response;
    }

}

const http = new HTTPWrapper();

function assembleListItem(taskName) {
    const listItem = document.createElement("li");
    listItem.classList = "task-row row-left-align spacing-between w100 thin-outline ";

    const checkbox = document.createElement("input");
    checkbox.className = "task-ch";
    checkbox.setAttribute("type", "checkbox");

    // tihs listener finds the checkbox who emitted "change" , and changes the style of sibling(paragraph)
    checkbox.addEventListener("change", e => {
        paragraph.style.textDecoration = e.target.checked ? 'line-through' : 'none';
        paragraph.style.fontWeight = e.target.checked ? 'normal' : 'bold';
    });

    const paragraph = document.createElement("p");
    paragraph.textContent = taskName;

    const deleteButton = document.createElement("button");
    deleteButton.setAttribute("type", "button");
    deleteButton.classList = "delete-btn";
    deleteButton.textContent = "Delete me!"

    deleteButton.addEventListener('click', async e => {
        await http.deleteTask(taskName);
        listItem.remove();
    });


    listItem.appendChild(checkbox);
    listItem.appendChild(paragraph);
    listItem.appendChild(deleteButton);

    return listItem;
}

async function createTask(taskName) {

    if (!taskName.trim()) {
        return;
    }

    const list = document.getElementById("task-list-div");
    const listItem = assembleListItem(taskName);

    // for creating new tasks, and writign them to db
    const response = await http.postTask(taskName);
    if (response.ok) {
        list.appendChild(listItem);
    }
    else {
        console.log("Skipping the render of this task, server cant process it");
    }
}

async function initTasksFromDatabase() {

    const response = await http.getExistingTasks();
    const taskObject = await response.json();
    const array = taskObject['result'];
    const list = document.querySelector('#task-list-div')
    array.forEach(async taskName => {
        list.append(assembleListItem(taskName));
    });

}

//! starting point-----------------------------------------------------------------------------------
// self explanatory i think
initTasksFromDatabase();



//event that fires only after the DOM is completely initialized
document.addEventListener("DOMContentLoaded", () => {
    // form allowed me to get the info from input field, and i insntantly convert it into the element 
    const form = document.querySelector("#task-form");
    form.addEventListener("submit", async e => {
        //ignores refreshing the page after "submit" event
        e.preventDefault();

        const button = document.querySelector("#add-btn");
        button.disabled = true;

        const taskNameFromField = new FormData(e.target).get('task-name');
        await createTask(taskNameFromField, false);

        button.disabled = false

    });

});

