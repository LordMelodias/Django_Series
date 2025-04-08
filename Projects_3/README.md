# BlogGlow

![BlogGlow Screenshot](https://via.placeholder.com/1200x600.png?text=BlogGlow+Screenshot)  
*A simple, elegant blog platform showcasing projects in Web Development, Data Analytics, and Cloud technologies.*

BlogGlow is a Django-based web application designed to display project stories in a visually appealing, responsive layout. It features categorized project sections, dynamic dates, estimated read times, and a toggle switch to alternate between Data Analytics and Cloud projects.

## Features
- **Categorized Projects**: Displays projects under three categories:
  - Web Development (always visible)
  - Data Analytics (default toggle state)
  - Clouds (toggle option)
- **Responsive Design**: Adapts seamlessly to desktop, tablet, and mobile devices.
- **Dynamic Content**: Shows actual project creation dates and estimated read times.
- **Toggle UI**: Switch between Data Analytics and Clouds with a sleek, animated toggle.
- **Image Handling**: Consistent 16:9 aspect ratio for project images with hover zoom effects.
- **Comments**: Allows anonymous commenting on project detail pages.
- **Modern Styling**: Uses Playfair Display and Roboto fonts, coral-themed gradients, and subtle animations.

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS (with custom styles), JavaScript (for toggle functionality)
- **Database**: SQLite (default, configurable to others)
- **Fonts**: Google Fonts (Roboto, Playfair Display)
- **Deployment**: Configurable for local development or production (e.g., with Gunicorn and PostgreSQL)

## Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtualenv (recommended)
- Git

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/blogglow.git
cd blogglow
