/**
 https://stackoverflow.com/questions/12388954/redirect-form-to-different-url-based-on-select-option-element
 used as reference to sort products with select element
*/
document.addEventListener('DOMContentLoaded', function() {
    const sortSelect = document.getElementById('sort-selector');
    
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            window.location.href = sortSelect.value;
        });
    }
});