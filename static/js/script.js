function getRecommendations() {
    const songName = document.getElementById('songInput').value;
    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({song: songName})
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error('Server error:', data.error);
        } else {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';
            data.forEach(track => {
                const div = document.createElement('div');
                div.innerHTML = `<img src="${track.image_url}" alt="Cover image" style="width:100px;height:100px;"><br>
                                 <strong class="song-name">${track.name}</strong><br>
                                 <span class="artist-name">Artist: ${track.artist}</span><br>
                                 Album: ${track.album}`;
                resultsDiv.appendChild(div);
            });
            
        }
    })
    .catch(error => console.error('Error:', error));
}
