console.log("JavaScript is working!");  // Check if script is loaded

const boardElement = document.getElementById('board');
let board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
];

// Render board and add click listeners
function renderBoard() {
    boardElement.innerHTML = '';  // Clear the board
    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            cell.textContent = board[row][col];
            cell.addEventListener('click', () => {
                console.log(`Clicked on row: ${row}, col: ${col}`);  // Debugging log
                handleMove(row, col);
            });
            boardElement.appendChild(cell);
        }
    }
}

async function handleMove(row, col) {
    console.log(`Cell clicked at row: ${row}, col: ${col}`);  // Confirm click is registered

    // Send POST request to /move endpoint
    const response = await fetch('/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            row: row,
            col: col,
            player: 'X'  // Sending the player's move (X or O)
        })
    });

    const data = await response.json();  // Parse the JSON response
    console.log("Response from server:", data);  // Log the response

    // Update the board with the new game state
    board = data.board;
    renderBoard();  // Re-render the board with updated state
    updateStatus(data.status);  // Update game status (e.g., win, draw, continue)
}
