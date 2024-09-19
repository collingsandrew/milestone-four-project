/* bag app */

/* credit: Code Institute - Boutique Ado project */

// update product quantity
document.querySelector('.update-link').addEventListener('click', function(e) {
    let form = this.previousElementSibling;
    
    if (form.classList.contains('update-form')) {
        form.submit();
    }
});

// remove product from bag
document.querySelector('.remove-item').addEventListener('click', function(e) {
    let csrfToken = "{{ csrf_token }}";
    let itemId = this.id.split('remove_')[1];
    let url = `/bag/remove/${itemId}`;
    let data = new FormData();
    data.append('csrfmiddlewaretoken', csrfToken);

    fetch(url, {
        method: 'POST',
        body: data
    })
    .then(response => {
        if (response.ok) {
            location.reload();
        } else {
            console.error('Error removing item');
        }
    })
    .catch(error => console.error('Error:', error));
});