/* bag app */

/* credit: Code Institute - Boutique Ado project */

// update product quantity
document.querySelectorAll('.update-link').forEach(function(updateLink) {
    updateLink.addEventListener('click', function(e) {
        let form = this.previousElementSibling;
        
        if (form.classList.contains('update-form')) {
            form.submit();
        }
    });
});

// remove product from bag
document.querySelectorAll('.remove-item').forEach(function(removeItem) {
    removeItem.addEventListener('click', function(e) {
        let csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;
        let itemId = this.id.split('remove_')[1];
        let url = `/bag/remove/${itemId}/`;
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
});

/* toasts */

/* credit: Code Institute - Boutique Ado project */

document.querySelectorAll('.toast').forEach(function (toastElement) {
    let toast = new bootstrap.Toast(toastElement);
    toast.show();
  });