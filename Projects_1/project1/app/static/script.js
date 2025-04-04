// static/script.js
console.log("Script version: 1.2 - Advanced Image UI");

function toggleForm() {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    loginForm.style.display = loginForm.style.display === 'none' ? 'block' : 'none';
    registerForm.style.display = registerForm.style.display === 'none' ? 'block' : 'none';
}

if (document.getElementById('loginForm')) {
    document.getElementById('loginForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = document.getElementById('loginEmail').value;
        const password = document.getElementById('loginPassword').value;
        
        const response = await fetch('login/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        
        const data = await response.json();
        const messageDiv = document.getElementById('loginMessage');
        
        if (response.ok) {
            messageDiv.innerHTML = 'Login successful!';
            localStorage.setItem('userEmail', data.email);
            window.location.href = 'home/';
        } else {
            messageDiv.innerHTML = data.error;
        }
    });
}

if (document.getElementById('registerForm')) {
    document.getElementById('registerForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const mobile = document.getElementById('mobile').value;
        const password = document.getElementById('password').value;
        
        const response = await fetch('register/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, email, mobile, password })
        });
        
        const data = await response.json();
        const messageDiv = document.getElementById('registerMessage');
        
        if (response.ok) {
            messageDiv.innerHTML = data.message;
        } else {
            messageDiv.innerHTML = data.error;
        }
    });
}

async function loadUserProfile() {
    console.log("loadUserProfile called");
    const email = localStorage.getItem('userEmail');
    if (!email) {
        console.log("No email in localStorage, redirecting to auth");
        window.location.href = '/';
        return;
    }

    try {
        const url = 'user-profile/?email=' + encodeURIComponent(email);
        console.log("Fetching from URL:", url);
        const response = await fetch(url, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        
        console.log("Response status:", response.status);
        const data = await response.json();
        console.log("Response data:", data);
        
        if (response.ok) {
            document.getElementById('username').textContent = data.username;
            document.getElementById('email').textContent = data.email;
            document.getElementById('mobile').textContent = data.mobile;
            
            const profileImage = document.getElementById('profileImage');
            const defaultLetter = document.getElementById('defaultLetter');
            const fullImage = document.getElementById('fullImage');
            if (data.profile_image) {
                profileImage.src = data.profile_image;
                fullImage.src = data.profile_image;
                profileImage.style.display = 'block';
                defaultLetter.style.display = 'none';
            } else {
                defaultLetter.textContent = data.username.charAt(0);
                profileImage.style.display = 'none';
                defaultLetter.style.display = 'block';
            }
        } else {
            console.log("Error response:", data.error);
            alert(data.error);
            window.location.href = '/';
        }
    } catch (error) {
        console.error("Fetch error:", error);
        alert("An error occurred while loading your profile");
        window.location.href = '/';
    }
}

// Advanced Image UI Handling
if (document.getElementById('profileImageWrapper')) {
    const viewImageBtn = document.getElementById('viewImage');
    const updateImageBtn = document.getElementById('updateImage');
    const imageUpdateModal = document.getElementById('imageUpdateModal');
    const imageViewModal = document.getElementById('imageViewModal');
    const closeModal = document.getElementById('closeModal');
    const closeViewModal = document.getElementById('closeViewModal');
    const dragDropArea = document.getElementById('dragDropArea');
    const fileInput = document.getElementById('profileImageInput');
    const imagePreview = document.getElementById('imagePreview');
    const previewImage = document.getElementById('previewImage');
    const cancelUpload = document.getElementById('cancelUpload');
    const confirmUpload = document.getElementById('confirmUpload');
    let selectedFile = null;

    // View Image
    viewImageBtn.addEventListener('click', () => {
        if (document.getElementById('profileImage').style.display === 'block') {
            imageViewModal.style.display = 'flex';
        }
    });

    // Update Image
    updateImageBtn.addEventListener('click', () => {
        imageUpdateModal.style.display = 'flex';
    });

    // Close Modals
    closeModal.addEventListener('click', () => {
        imageUpdateModal.style.display = 'none';
        resetUploadUI();
    });

    closeViewModal.addEventListener('click', () => {
        imageViewModal.style.display = 'none';
    });

    // Click outside to close modals
    window.addEventListener('click', (e) => {
        if (e.target === imageUpdateModal) {
            imageUpdateModal.style.display = 'none';
            resetUploadUI();
        } else if (e.target === imageViewModal) {
            imageViewModal.style.display = 'none';
        }
    });

    // Open file input on browse click
    dragDropArea.querySelector('.browse-link').addEventListener('click', () => {
        fileInput.click();
    });

    // Handle file selection
    fileInput.addEventListener('change', (e) => {
        handleFile(e.target.files[0]);
    });

    // Drag and Drop Events
    dragDropArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        dragDropArea.classList.add('dragover');
    });

    dragDropArea.addEventListener('dragleave', () => {
        dragDropArea.classList.remove('dragover');
    });

    dragDropArea.addEventListener('drop', (e) => {
        e.preventDefault();
        dragDropArea.classList.remove('dragover');
        handleFile(e.dataTransfer.files[0]);
    });

    function handleFile(file) {
        if (file && file.type.startsWith('image/')) {
            selectedFile = file;
            const reader = new FileReader();
            reader.onload = (e) => {
                previewImage.src = e.target.result;
                imagePreview.style.display = 'block';
                dragDropArea.style.display = 'none';
            };
            reader.readAsDataURL(file);
        } else {
            alert('Please select a valid image file');
        }
    }

    // Cancel Upload
    cancelUpload.addEventListener('click', () => {
        resetUploadUI();
    });

    // Confirm Upload
    confirmUpload.addEventListener('click', async () => {
        if (!selectedFile) return;

        const email = localStorage.getItem('userEmail');
        const formData = new FormData();
        formData.append('email', email);
        formData.append('profile_image', selectedFile);

        try {
            const response = await fetch('update-profile-image/', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            if (response.ok) {
                const profileImage = document.getElementById('profileImage');
                const fullImage = document.getElementById('fullImage');
                const defaultLetter = document.getElementById('defaultLetter');
                profileImage.src = data.profile_image;
                fullImage.src = data.profile_image;
                profileImage.style.display = 'block';
                defaultLetter.style.display = 'none';
                imageUpdateModal.style.display = 'none';
                resetUploadUI();
                alert('Profile image updated!');
            } else {
                alert(data.error);
            }
        } catch (error) {
            console.error("Image upload error:", error);
            alert("An error occurred while updating your profile image");
        }
    });

    function resetUploadUI() {
        selectedFile = null;
        imagePreview.style.display = 'none';
        dragDropArea.style.display = 'block';
        fileInput.value = '';
    }
}

function logout() {
    localStorage.removeItem('userEmail');
    window.location.href = '/';
}

if (window.location.pathname === 'home/') {
    window.addEventListener('load', loadUserProfile);
}