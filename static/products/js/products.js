/**
 https://usefulangle.com/post/81/javascript-change-url-parameters
 used as reference to sort products with select element
*/
document.addEventListener('DOMContentLoaded', function() {
    const sortSelect = document.getElementById('sort-selector');
    
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            const selectedValue = sortSelect.value;
            const currentUrl = new URL(window.location.href);
            
            currentUrl.searchParams.set('sort', selectedValue);

            window.location.href = currentUrl.toString();
        });
    }
});