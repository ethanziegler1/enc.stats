# enc.stats 🎵 

A lightweight **Flask** web application that connects to a user's **Spotify account** and provides a detailed rundown of their listening habits. Built with **Spotipy**, this app fetches and displays top artists, albums, and tracks over different time ranges.  

## 🚀 Features  
- 🔑 **Spotify OAuth Authentication** – Secure login via Spotify  
- 🎶 **Top Artists & Tracks** – View your most listened-to content  
- ⏳ **Custom Time Ranges** – Short-term, medium-term, and long-term stats  
- ⚡ **Minimal & Fast** – Small Flask backend with efficient API calls  

## 🛠 Tech Stack  
- **Backend:** Python (Flask, Spotipy)  
- **API:** Spotify Web API  
- **Frontend:** HTML, CSS, JavaScript  
- **Deployment:** Works with **Render, Heroku, or any Flask-compatible platform**  

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
   
![image](https://github.com/user-attachments/assets/058f808a-b9ed-41b5-8e52-630140bc9406)


2.**Then you will be routed to Spotify's OAuth page that verifies the user exists in Spotify's databases**

![image](https://github.com/user-attachments/assets/3d2fd1fd-8982-4126-af5f-06902422f387)


3.**Finally, all of your data is shown in a neat and user-friendly way with options to see top artists, songs, or albums**

![image](https://github.com/user-attachments/assets/fa9dce66-7bc5-4bca-9878-219aae632af6)
