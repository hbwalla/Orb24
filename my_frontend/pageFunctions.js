
// const box = document.createElement("div");
// box.style.backgroundColor = "blue";
// box.style.width = 100;
// box.style.height = 100;
// box.style.position
// const element = document.getElementById("container");
// element.appendChild(box)

$(document).ready(function() { 
    // Get the div element by its ID 
    var $div = $('<div> Testing! </div>', {id: "foo", "class": "a"}); 
    $div.css({
        "background-color": '#bcd500',
        "width": "100px",
        "height": "15px",
        "z-index": "10",
        "left": "300px",
        "top": "300px",
        "position": "fixed",
        "text-align": "center",
        "font-family": "Arial Bold",
        "border-radius": "5px",
        "color": "#151514",
        "padding": "10px"
    });

    $(function() {
        $(".a").draggable();
    });
    
    $("#container").append($div);
  }); 
