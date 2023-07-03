# Route to handle the video upload
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        file.save('static/' + file.filename)
        return 'Video uploaded successfully!'
    else:
        return 'No video selected!'
