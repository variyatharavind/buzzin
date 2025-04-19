// Modal logic
const modal = document.getElementById('modal');
const closeModalBtn = document.getElementById('close-modal');
const showAnswerBtn = document.getElementById('show-answer');
const modalCategory = document.getElementById('modal-category');
const modalValue = document.getElementById('modal-value');
const modalQuestion = document.getElementById('modal-question');
const modalAnswer = document.getElementById('modal-answer');

let currentCell = null;

// Show modal with question
function showQuestion(cell) {
    modalCategory.textContent = cell.dataset.category;
    modalValue.textContent = `$${cell.dataset.value}`;
    modalQuestion.textContent = cell.dataset.question;
    modalAnswer.textContent = cell.dataset.answer;
    modalAnswer.style.display = 'none';
    showAnswerBtn.style.display = '';
    modal.style.display = 'block';
}

document.querySelectorAll('.cell').forEach(cell => {
    cell.addEventListener('click', function() {
        if (cell.classList.contains('cell-used')) return;
        currentCell = cell;
        showQuestion(cell);
    });
});

closeModalBtn.onclick = function() {
    modal.style.display = 'none';
    if (currentCell) {
        const mock = document.createElement('div');
        mock.className = 'cell-mock';
        currentCell.parentNode.replaceChild(mock, currentCell);
        currentCell = null;
    }
};

showAnswerBtn.onclick = function() {
    modalAnswer.style.display = '';
    showAnswerBtn.style.display = 'none';
};

window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = 'none';
        if (currentCell) {
            currentCell.parentNode.removeChild(currentCell);
            currentCell = null;
        }
    }
};
