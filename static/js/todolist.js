$(document).ready( function() {

    // this code will be executed only the DOM is fully loaded

    $('div.jumbotron').click( function() {

        // code that is executed when che jumbotron is clicked
        alert("Got you!") ;
    } ) ;

    $('form').submit( function(event) {
        // validate the form

        $('div#errorbox').empty() ;
        var text = $("input[name='description']").val() ;

        if(text.length < 3) {
            $('div#errorbox').text("Description too short").addClass("text-danger") ;
            $("input[name='description']").parent().addClass("has-error") ;
            window.setTimeout( function() {
                $("input[name='description']").parent().removeClass("has-error") ;
            } , 1000) ;
            event.preventDefault() ;
        }
    } ) ;
} ) ;