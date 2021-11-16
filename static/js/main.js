
//Board's Card Function

//task sortable
const sortable = new Draggable.Sortable(
    document.querySelectorAll("ul"),
    { draggable: "li" }
);

//cat sortable
const sortableCat = new Draggable.Sortable(
    document.querySelectorAll(".main-div"),
    { draggable: ".category-swap", handle: ".card-header" }
);