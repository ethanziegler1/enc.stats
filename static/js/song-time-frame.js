document.addEventListener("DOMContentLoaded", () => {
    let songList = document.querySelector("#song-list");
    let top_songs = songList.dataset.top_songs;

    for (let i = 0; i < top_songs; i++) {
        let li = document.createElement("li");
        li.innerText = `Song ${i}`;
        songList.appendChild(li);
    }
});
