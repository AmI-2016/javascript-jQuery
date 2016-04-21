function titleClicked() {
    alert("Oouch!") ;
}

function checkForm() {
    var input = document.getElementById("descriptioninput") ;
    var text = input.value ;
    if(text.length != 0)
        return true ;
    else {
        alert("Error: empty text");
        return false ;
    }

}