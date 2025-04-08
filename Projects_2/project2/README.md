# Voice Call App

A real-time voice calling application built with Django and PeerJS, featuring a modern UI with call controls like mute, speaker toggle, and hang-up, along with a live call timer. This app allows users to log in, see a list of other users, and initiate voice calls over a local network using WebRTC.

## Features
- User authentication (login/logout)
- List of available users with "Call" buttons
- Full-screen call UI with:
  - Avatar display
  - Call status (e.g., "Calling", "Connected")
  - Real-time call duration timer
  - Call controls: Mute, Speaker, Hang Up
- Responsive design for PC and mobile
- Secure HTTPS connection for WebRTC

## Technologies Used

| Technology            | Purpose                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| **Django**            | Backend framework for user authentication, API endpoints, and serving the app |
| **Python**            | Programming language for Django backend logic                          |
| **PeerJS**            | Simplified WebRTC library for peer-to-peer voice calls                 |
| **WebRTC**            | Real-time communication protocol for audio streaming between peers     |
| **JavaScript**        | Client-side logic for PeerJS, WebRTC, and UI interactions              |
| **HTML/CSS**          | Structure and styling of the user interface                            |
| **Font Awesome**      | Icons for call control buttons (Mute, Speaker, Hang Up)                |
| **Node.js**           | Runs the PeerJS server for signaling between peers                     |
| **django-extensions** | Provides `runserver_plus` for HTTPS support in development            |
| **OpenSSL**           | Generates self-signed SSL certificates for HTTPS                      |

### Technology Details
- **Django**: Manages user authentication, serves the user list via an API (`/api/users/`), and logs call attempts (`/api/call/`).
- **PeerJS**: Handles peer-to-peer connections, simplifying WebRTC setup and signaling via a local PeerJS server.
- **WebRTC**: Enables direct audio communication between browsers, requiring HTTPS for security (except on `localhost`).
- **JavaScript**: Controls the call flow (initiate, answer, hang up), manages the UI (e.g., timer, button states), and integrates PeerJS/WebRTC.
- **HTML/CSS**: Creates a modern, responsive UI with a gradient background, user cards, and a full-screen call overlay.
- **Font Awesome**: Adds professional icons to enhance the call control buttons.
- **Node.js**: Powers the PeerJS server (`peerjs --port 9000`) for coordinating peer connections.
- **django-extensions**: Extends Django with `runserver_plus` to serve the app over HTTPS using self-signed certificates.
- **OpenSSL**: Used to create `cert.pem` and `key.pem` for local HTTPS testing.

## How It Works

1. **Setup**:
   - The Django backend runs on `https://192.168.0.106:8000` (replace with your PC’s IP) using `runserver_plus` and self-signed SSL certificates.
   - A PeerJS server runs on `192.168.0.106:9000` for signaling between peers.

2. **User Authentication**:
   - Users log in via Django’s authentication system to access the user list page (`/users/`).

3. **User List**:
   - The frontend fetches the list of users from `/api/users/` and displays them as cards with "Call" buttons.

4. **Initiating a Call**:
   - Clicking "Call" triggers `navigator.mediaDevices.getUserMedia` to access the microphone.
   - PeerJS initiates a call to the receiver’s peer ID (e.g., `peer-2`) via the local PeerJS server.

5. **Call UI**:
   - A full-screen overlay appears with the receiver’s avatar, call status, timer, and controls (Mute, Speaker, Hang Up).
   - The timer starts, updating every second.

6. **Receiving a Call**:
   - The receiver gets a confirmation prompt and, upon accepting, connects via WebRTC.
   - Both sides see the call UI with active controls.

7. **Call Controls**:
   - **Mute**: Toggles the microphone on/off.
   - **Speaker**: Simulates speaker toggle (visual only; actual routing is browser-dependent).
   - **Hang Up**: Closes the call, stops audio tracks, and resets the UI.

8. **Ending a Call**:
   - Either user clicks "Hang Up," closing the PeerJS connection and resetting the UI.

## Prerequisites
- Python 3.12+
- Node.js 16+
- OpenSSL (for generating SSL certificates)
- Git
