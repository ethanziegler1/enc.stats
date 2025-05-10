document.addEventListener("DOMContentLoaded", () => {
    let songListContainer = document.querySelector("#song-list-container");
    console.log(songListContainer);

    let topSongs = songListContainer.dataset.topSongs;
    console.log(topSongs);

    topSongs.forEach((song, index) => {
        let li = document.createElement("li");
        li.innerHTML = `
            <span>${index + 1}.</span>
            <img src="${song.album.images[0].url}" alt="${song.name}" width="50" height="50" />
            <p>${song.name} - ${song.artists[0]?.name || 'Unknown Artist'}</p>
        `;
        songListContainer.appendChild(li);
    });
});