document.getElementById('uploadForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const resultDiv = document.getElementById('result');

    resultDiv.innerHTML = '<p>Uploading...</p>';

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultDiv.innerHTML = `<p style="color: red;">${data.error}</p>`;
        } else {
            resultDiv.innerHTML = `<p>${data.message}</p>`;
            data.paths.forEach(path => {
                resultDiv.innerHTML += `<p>Uploaded Path: ${path}</p><br> <video><source src="${path}"></video>`;
            });
        }
    })
    .catch(error => {
        resultDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
    });
});