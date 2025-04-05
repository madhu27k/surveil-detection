import os
from flask import Flask, request, render_template, jsonify, send_from_directory
from hello import pre
from object_detector import modelrun
app = Flask(__name__)
# Directory for uploads
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload_videos():
    if 'videos' not in request.files:
        return jsonify({'error': 'No video files provided'}), 400
    # Get all uploaded files
    video_files = request.files.getlist('videos')
    if not video_files or all(video.filename == '' for video in video_files):
        return jsonify({'error': 'No files selected'}), 400
    # Save files and collect their paths
    uploaded_paths = []
    for video in video_files:
        if video and video.filename:
            file_path = os.path.join('uploads/', video.filename)
            video.save(file_path)
            uploaded_paths.append(file_path)
            pre()
            pre()
            print(file_path)
            modelrun(file_path)
            pre()
    video_to_display = uploaded_paths[0] if uploaded_paths else None
    return render_template('vid.html', video_path=video_to_display)        
    return jsonify({
        'message': 'Videos uploaded successfully <h1>test</h1> <video><source src="uploads/youtube_xm5YYY-4Dp8_720x1280_h264.mp4"></video><h1>test</h1>',
        'paths': uploaded_paths,
        'html':"<h1>cry for help</h1>"
    })
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)