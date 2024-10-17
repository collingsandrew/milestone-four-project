/*
Country field
update country field colour, depending on whether a country is selected or not
*/

// get the default country element
let defaultCountry = document.getElementById('id_default_country');

// set initial color based on selected value
if (!defaultCountry.value) {
    defaultCountry.style.color = '#aab7c4';
}

// add change event listener
defaultCountry.addEventListener('change', function() {
    if (!this.value) {
        this.style.color = '#aab7c4';
    } else {
        this.style.color = '#3C3A36';
    }
});