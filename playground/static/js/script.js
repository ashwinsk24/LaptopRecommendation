const icon= document.querySelector('.icon');
const search = document.querySelector('.search');
icon.onclick = function() {
    search.classList.toggle('active');
}


function submitForm(event) {
    event.preventDefault();  // Prevent the form from submitting normally
    var form = event.target;
    var input = form.elements.search_query;
    var query = input.value.trim();
    if (query !== '') {
        var url = 'https://www.google.com/search?q=' + encodeURIComponent(query);
        window.location.href = url;
    }
    return false;
}


var input = document.querySelector('input[name="search_query"]');
    input.addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            event.target.form.submit();
        }
    });