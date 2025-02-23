document.addEventListener("DOMContentLoaded", function() {
    fetch('/expenses')
        .then(response => response.json())
        .then(data => {
            let categories = {};
            data.forEach(expense => {
                categories[expense.category] = (categories[expense.category] || 0) + expense.amount;
            });

            const ctx = document.getElementById("expenseChart").getContext("2d");
            new Chart(ctx, {
                type: "pie",
                data: {
                    labels: Object.keys(categories),
                    datasets: [{
                        data: Object.values(categories),
                        backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#4CAF50", "#F44336"]
                    }]
                }
            });
        });
});
