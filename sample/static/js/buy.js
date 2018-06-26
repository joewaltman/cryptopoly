
$(window).bind("load", function() {
    console.log( "ready!" );
    isPropertyOwned($("#status").attr("venueId"))
    .then(function(isOwned){
        if(isOwned){
            console.log("Property already owned");
            $("#status").html('Property already owned');
            $("#status").attr("disabled", "disabled");
        }
        else{
            console.log("Property free tobuy");
            $("#status").attr("disabled", false)
            $("#status").html('Buy');
        }


    });

});


$("#status").click(function(){
    console.log("Buy this property");
    buyProperty($(this).attr("name"), $(this).attr("latitude"), $(this).attr("longitude"), $(this).attr("venueId"));
})