document.addEventListener("DOMContentLoaded", function() {
    fetch('/expenses')
        .then(response => response.json())
        .then(data => {
            const expensesDiv = document.getElementById('expenses');
            data.forEach(expense => {
                let item = document.createElement('p');
                item.textContent = `${expense.date}: ${expense.description} - ${expense.amount}$`;
                expensesDiv.appendChild(item);
            });
        });

    document.getElementById("addExpense").addEventListener("click", function() {
        const description = document.getElementById("description").value;
        const category = document.getElementById("category").value;
        const amount = document.getElementById("amount").value;
        const date = document.getElementById("date").value;

        fetch('/expenses', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ description, category, amount, date })
        }).then(response => response.json())
        .then(data => {
            alert("Expense added successfully!");
            location.reload();
        });
    });
});
