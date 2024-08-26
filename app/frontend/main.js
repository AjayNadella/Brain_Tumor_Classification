document.getElementById('uploadForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Please upload an image file.');
        return;
    }
    
    const imagePreview = document.getElementById('imagePreview');
    imagePreview.src = URL.createObjectURL(file);
    imagePreview.style.display = 'block';
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        const response = await fetch('/predict/', {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        const result = await response.json();
        
        document.getElementById('predictedClass').textContent = 'Predicted Class: ' + result.predicted_class;
        document.getElementById('confidence').textContent = 'Confidence: ' + result.confidence + '%';
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('predictedClass').textContent = 'Error: ' + error.message;
        document.getElementById('confidence').textContent = '';
    }
});
