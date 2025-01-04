document.addEventListener("DOMContentLoaded", function() {
    const rows = document.querySelectorAll(".styled-table tbody tr");

    rows.forEach(row => {
        row.addEventListener("click", function() {
            alert(`Produto: ${this.cells[0].textContent}, Valor: ${this.cells[1].textContent}`);
        });
    });
});
