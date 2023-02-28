
//retrieve pledge report from back-end and display on front-end.
function getPledgeReport() {
    var url = "http://localhost:5000/api/pledges/"

    $.get(url, function(data, status){
        //console.log(data, status);
        var result = "<table class='table table-dark table-hover'>";
        for(var i = 0; i < data.length; i++) {
            result += "<tr><td>" + data[i].first_name + " " + data[i].last_name + "</td><td>$" + data[i].amount + "</td><td>" + data[i].datetime + "</td></tr>";
        }
        result += "</table>"
        $("#results_container").html(result);
    });    
}


//take pledge data from the front-end and post it to the back-end.
function addNewPledge() {
    var firstName = $("#firstName").val();
    var lastName = $("#lastName").val();
    var town = $("#town").val();
    var province = $("#province").val();
    var postalCode = $("#postalCode").val();
    var email1 = $("#email1").val();
    var email2 = $("#email2").val();
    var amount =$("#amount").val();
    if (email1 == email2 && firstName !="" && lastName != "" && town != "" && province != "" && postalCode != "" && amount != "" && email1 != "") {
    var new_entry = {
        //retrieve (from the UI) field values and add them to a new entry here
        //
        "first_name" : firstName,
        "last_name" : lastName,
        "town": town,
        "province" : province,
        "postalCode" : postalCode,
        "email" : email1,
        "amount" : amount,
        "datetime" : new Date().getFullYear() + "-" + (new Date().getMonth()+1) + "-" + new Date().getDate()
    };
    console.log(new_entry);
    //ajax using POST method to put new_entry up to http://localhost:5000/api/pledges
    //
    const firstNameBox = document.getElementById('firstName');
    const lastNameBox = document.getElementById('lastName');
    const townBox = document.getElementById('town');
    const provinceBox = document.getElementById('province');
    const postalCodeBox = document.getElementById('postalCode');
    const email1Box = document.getElementById('email1');
    const email2Box = document.getElementById('email2');
    const amountBox = document.getElementById('amount');
    $.ajax({
        type: "POST",
        url: "http://localhost:5000/api/pledges",
        data: JSON.stringify(new_entry),
        contentType: "application/json",
        dataType: "json",
        success: function(data) {
            alert("Pledge Sent Succesfully!")
            
            firstNameBox.value = '';
            lastNameBox.value = '';
            townBox.value = '';
            provinceBox.value = '';
            postalCodeBox.value = '';
            email1Box.value = '';
            email2Box.value = '';
            amountBox.value = '';
        },
        error: function(error) {
            
            alert("error");
             }
        });
    } else {
        alert("Make sure Emails match and all fields are filled out!")
    }

}