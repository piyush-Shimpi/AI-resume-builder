from flask import Flask, request, render_template, send_file
from utils.parser import extract_resume, extract_jd_keywords
from utils.generator import generate_custom_resume

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resume_file = request.files['resume']
        jd_text = request.form['job_description']

        resume_data = extract_resume(resume_file)
        jd_keywords = extract_jd_keywords(jd_text)
        optimized_resume = generate_custom_resume(resume_data, jd_keywords)

        # Save or export function
        out_file = save_resume_as_docx(optimized_resume)
        return send_file(out_file, as_attachment=True)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
