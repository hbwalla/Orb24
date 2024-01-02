console.log("Hello from app.js!");

// document.addEventListener("DOMContentLoaded", (event) => {
//     document.querySelectorAll(".draggable").forEach((element) => {
//         element.addEventListener("dragstart", function(e) {
//             e.dataTransfer.setData("text", this.id);
//         });
//     });

//     let dropZone = document.getElementById("drop-zone");

//     dropZone.addEventListener("drop", function(e) {
//         e.preventDefault();
//         this.classList.add("over");
//         // let data = e.dataTransfer.getData("text");
//         // e.target.appendChild(document.getElementById(data));
//     });

//     dropZone.addEventListener("dragleave", function(e) {
//         this.classList.remove("over");
//     });

//     dropZone.addEventListener("drop", function(e) {
//         e.preventDefault();
//         this.classList.remove("over");

//         let data = e.dataTransfer.getData("text");
//         let draggableElement = document.getElementById(data);
//         this.innerHTML = "Dropped: ${draggableElement.textContent}";
//     });
// });

document.addEventListener('DOMContentLoaded', (event) => {
    // Drag start event listener
    document.querySelectorAll('.draggable').forEach((element) => {
        element.addEventListener('dragstart', function(e) {
            e.dataTransfer.setData('text', this.id); // Set the drag data
        });
    });

    // Drop zone element
    let dropZone = document.getElementById('drop-zone');

    // Drag over event listener
    dropZone.addEventListener('dragover', function(e) {
        e.preventDefault(); // Allow a drop
        this.classList.add('over'); // Add a class for visual feedback
    });

    // Drag leave event listener
    dropZone.addEventListener('dragleave', function(e) {
        this.classList.remove('over'); // Remove the visual feedback class
    });

    // Drop event listener
    dropZone.addEventListener('drop', function(e) {
        e.preventDefault();
        this.classList.remove('over'); // Remove the visual feedback class

        let data = e.dataTransfer.getData('text');
        let draggableElement = document.getElementById(data);
        this.innerHTML = `Dropped: ${draggableElement.textContent}`; // Update drop zone content
    });
});