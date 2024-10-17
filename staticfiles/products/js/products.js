/**
 https://usefulangle.com/post/81/javascript-change-url-parameters
 used as reference to sort products with select element
*/
document.addEventListener('DOMContentLoaded', function() {
    // sorting functionality
    const sortSelect = document.getElementById('sort-selector');
    
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            const selectedValue = sortSelect.value;
            const currentUrl = new URL(window.location.href);
            
            currentUrl.searchParams.set('sort', selectedValue);

            window.location.href = currentUrl.toString();
        });
    }

    // scroll to top of page functionality
    const backToTopLink = document.querySelector('.btt-link');
    
    if (backToTopLink) {
        backToTopLink.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});