
const taskInfo = {};

document.addEventListener("DOMContentLoaded", () => {

    const taskList = document.getElementById("task-list-div");

    taskList.addEventListener("change", e => {
        const element = e.target;

        if (!taskInfo[element.id]) {
            taskInfo[element.id] = element.nextElementSibling.textContent;
        }

        element.nextElementSibling.textContent = element.checked
            ? "Task \"" + taskInfo[element.id] + "\" is done!"
            : taskInfo[element.id];

        element.nextElementSibling.style.textDecoration = element.checked ? 'line-through' : 'none';
        element.nextElementSibling.style.fontWeight = element.checked ? 'normal' : 'bold';
    });

    taskList.addEventListener("click", e => {
        const element = e.target;
        if (element.classList.contains("delete-btn")) {
            element.parentElement.remove();
        }
    });

    const form = document.querySelector("#task-form");
    form.addEventListener("submit", e => {
        e.preventDefault();
        const data = new FormData(e.target);
        const name = data.get("task-name");


        const list = document.getElementById("task-list-div");

        const listItem = document.createElement("li");
        listItem.classList = "task-row row-left-align spacing-between w100 thin-outline ";

        const checkbox = document.createElement("input");
        checkbox.className = "task-ch";
        checkbox.setAttribute("type", "checkbox");
        checkbox.id = "t" + Object.keys(taskInfo).length.toString();

        const taskName = document.createElement("p");
        taskName.textContent = data.get("task-name");

        const deleteButton = document.createElement("button");
        deleteButton.setAttribute("type", "button");
        deleteButton.classList = "delete-btn";
        deleteButton.textContent = "Delete me!"

        taskInfo[checkbox.id] = taskName.textContent;

        listItem.appendChild(checkbox);
        listItem.appendChild(taskName);
        listItem.appendChild(deleteButton);

        list.appendChild(listItem);
    });

});

