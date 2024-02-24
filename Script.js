const Display = document.getElementById("Display");

function AppendToDisplay(Input){
    Display.value += Input;
}


function ClearDisplay(){
    Display.value = "";
}

function Calculate(){
    Display.value = eval(Display.value);
}





