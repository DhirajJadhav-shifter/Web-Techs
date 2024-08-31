document.getElementById('searchButton').addEventListener('click', function() {
    var placesList = document.getElementById('placesList');
    if (placesList.classList.contains('hidden')) {
        placesList.classList.remove('hidden');
    } else {
        placesList.classList.add('hidden');
    }
});
