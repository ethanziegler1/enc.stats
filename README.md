# 🎵 enc.stats 

A lightweight **Flask** web application that connects to a user's **Spotify account** and provides a detailed rundown of their listening habits. Built with **Spotipy**, this app fetches and displays top artists, albums, and tracks over different time ranges.  

## 🚀 Features  
- 🔑 **Spotify OAuth Authentication** – Secure login via Spotify  
- 🎶 **Top Artists & Tracks** – View your most listened-to content  
- ⏳ **Custom Time Ranges** – Short-term, medium-term, and long-term stats  
- ⚡ **Minimal & Fast** – Small Flask backend with efficient API calls  

## 🛠 Tech Stack  
- **Backend:** Python (Flask)  
- **API:** Spotify Web API  (using Spotipy Python Package)
- **Frontend:** HTML, CSS

## 📥 Installation & Setup  

1. **Clone the repository:**  
   ```sh
   git clone https://github.com/cpritt/spotipy-flask-app.git  
   cd enc.stats
2. **Install Requirements into a Virtual Environment of your choice**
   ```sh
   pip install -r requirements.txt
3. **Run the Web application**
   python main.py

## Demo
**Since enc.stats does not have the required user base for Spotify to give us an Authorization Extension, only verfied users can sign in to enc.stats**
**Here is a demonstration of what our app provides the user!**
1. **First you are prompted with a welcome screen that gives you the option to sign into Spotify**
   
![Screenshot 2025-03-18 171454](https://github.com/user-attachments/assets/28448fdb-e52f-4af0-8a99-cc840d6b59e3)



2.**Then you will be routed to Spotify's OAuth page that verifies the user exists in Spotify's databases**

![Screenshot 2025-03-18 171518](https://github.com/user-attachments/assets/0e1ab8d3-081e-4fad-9f65-7c55acc93d55)



3.**Finally, all of your data is shown in a neat and user-friendly way with options to see top artists, songs, or albums**

![Screenshot 2025-03-18 171748](https://github.com/user-attachments/assets/fca69d5a-6e28-4ba7-adf8-2166e856888b)

