// $(function() {
//     // $("#option-class").draggable({})
//     //     revert: "invalid",
//     //     stack: ".draggable",
//     //     helper: "clone"
//     // });
//     $("#option-class").click(function(event) {
//         // alert("hello!");
//         $(".container").prepend(".class-clone");
//         event.stopImmediatePropagation();
//     });
// });

// $(function() {
//     $("#option-class-clone").draggable({});
// });

$(function() {
    $("#option-class").draggable();
});

$(function() {
    $("#option-function").draggable();
});

$(function() {
    $("#option-dictionary").draggable();
});

$(function() {
    $("#option-property").draggable();
});

$(function() {
    $("#option-string").draggable();
});

$(function() {
    $("#option-boolean").draggable();
});

$(function() {
    $("#option-argument").draggable();
});

$(function() {
    $("#option-integer").draggable();
});

$(function() {
    $("#option-float").draggable();
});

$(function() {
    $("#option-list").draggable();
});

$(function() {
    $("#option-array").draggable();
});

$(function() {
    $("#option-set").draggable();
});

$(function() {
    $("#option-tuple").draggable();
});

$("#container").droppable({
    accept: '.class',
    drop: function(event, ui) {
        $(this).append($("ui.draggable").clone());
        $("#container .class").addClass("item");
        $(".item").removeClass("ui-draggable product");
        $(".item").draggable({
            containment: 'parent',
            grid: [150, 150]
        });
    }
});
$(".class").draggable({
    helper: 'clone'
});

// const {ReactDraggable: Draggable, React, ReactDOM} = window;

// class App extends React.Component {
//     state = {
//         activeDrags: 0,
//         deltaPosition: {x: 0, y: 0},
//         controlledPosition: {x: -400, y: 200}
//     };
//     handleDrag = (e, ui) => {
//         const {x, y} = this.state.deltaPosition;
//         this.setState({
//             deltaPosition: {x: x + ui.deltaX, y: y + ui.deltaY}
//         });
//     };
    
//     onStart = () => {
//         this.setState({activeDrags: ++this.state.activeDrags});
//     };

//     onStop = () => {
//         this.setState({activeDrags: --this.state.activeDrags});
//     };

//     onDrop = (e) => {
//         this.setState({activeDrags: --this.state.activeDrags});
//         if (e.target.classList.contains("drop-target")) {
//             alert("Dropped");
//             e.target.classList.remove("hovered");
//         }
//     };

//     onDropAreaMouseEnter = (e) => {
//         if (this.state.activeDrags) {
//           e.target.classList.add('hovered');
//         }
//     }
    
//     onDropAreaMouseLeave = (e) => {
//         e.target.classList.remove('hovered');
//     }
    
//       // For controlled component
//     adjustXPos = (e) => {
//         e.preventDefault();
//         e.stopPropagation();
//         const {x, y} = this.state.controlledPosition;
//         this.setState({controlledPosition: {x: x - 10, y}});
//     };
    
//     adjustYPos = (e) => {
//         e.preventDefault();
//         e.stopPropagation();
//         const {controlledPosition} = this.state;
//         const {x, y} = controlledPosition;
//         this.setState({controlledPosition: {x, y: y - 10}});
//     };
    
//     onControlledDrag = (e, position) => {
//         const {x, y} = position;
//         this.setState({controlledPosition: {x, y}});
//     };
    
//     onControlledDragStop = (e, position) => {
//         this.onControlledDrag(e, position);
//         this.onStop();
//     };
    

// }



// function onDragStart(event) {
//     event
//         .dataTransfer
//         .setData("text", event.target.id);
//     event
//         .currentTarget
//         .style
// }

// function onDragOver(event) {
//     event.preventDefault();
// }

// function onDrop(event) {
//     const id = event
//         .dataTransfer
//         .getData("text")
//     const draggableElement = document.getElementById(id);
//     const dropzone = event.target;
//     dropzone.appendChild(draggableElement);
//     draggableElement.style.position = "absolute";
//     event
//         .dataTransfer
// }

// // -------

// // function onDragStart(event) {
// //     event
// //         .dataTransfer
// //         .setData("text/plain", event.target.id);
    
// //     event
// //         .currentTarget
// //         .style
// //         .backgroundColor = "yellow";
// // }

// // function onDragOver(event) {
// //     event.preventDefault();
// // }

// // function onDrop(event) {
// //     const id = event
// //         .dataTransfer
// //         .getData("text");
// //     const draggableElement = document.getElementById(id);
// //     const dropzone = event.target;
// //     dropzone.appendChild(draggableElement);
// //     event
// //         .dataTransfer
// //         .clearData();
// // }

// function onClassOptionClick() {
//     alert("Class button clicked!");
// }
// const classOption = document.getElementById("option-class");
// classOption.addEventListener("click", onClassOptionClick());


// function onShapeButtonClick() {
//     alert("Shape button clicked!");
// }
// const squareButton = document.getElementById("square");
// squareButton.addEventListener("click", onShapeButtonClick);


// function onArrowButtonClick() {
//     alert("Arrow button clicked!");
// }
// const arrowButton = document.getElementById("arrow");
// arrowButton.addEventListener("click", onArrowButtonClick);


// function onArrowButtonClick() {
//     alert("Arrow button clicked!");
// }
// const arrowButtun = document.getElementById("arrow");
// arrowButton.addEventListener("click", onArrowButtonClick);

