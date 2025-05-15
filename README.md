<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

  <h1>📄🖼️ Image Text Extraction API - DRF</h1>
    <p class="status">⚠️ This project is still under development ⚠️</p>
    <p>The Image Text Extraction API - DRF is an OCR (Optical Character Recognition) API built with Django REST Framework. Its goal is to extract readable text from images, serving as a foundation for applications like data automation, document analysis, and accessibility tools.</p>

  <h2>🛠 STAR Methodology</h2>

  <h3>🏞️ Situation</h3>
    <p>Manually extracting text from images, such as scanned documents, receipts, or ID cards, is time-consuming and prone to errors.</p>

  <h3>🎯 Task</h3>
    <p>Develop a REST API that receives an image and automatically returns the extracted text using OCR technologies.</p>

  <h3>🏃‍♂️ Action</h3>
    <ul>
        <li>Built a REST API using Django REST Framework.</li>
        <li>Implemented Tesseract as the OCR engine.</li>
        <li>Structured endpoints for future integration with a React frontend.</li>
        <li>Prepared the foundation for user authentication and access control.</li>
    </ul>

  <h3>🎯 Result</h3>
    <ul>
        <li>The API can now process images via an endpoint and return extracted text.</li>
        <li>Ready for integration with web applications.</li>
        <li>Scalable for future enhancements, such as authentication, permissions, and advanced features.</li>
    </ul>

  <h2>🚀 How to Run the Project</h2>

  <h3>1. Clone the Repository</h3>
    <pre><code>git clone https://github.com/kailanesarah/image-text-extraction-API-DRF.git
cd image-text-extraction-API-DRF</code></pre>

  <h3>2. Configure Environment Variables</h3>
    <pre><code>DJANGO_SECRET_KEY='your_secret_key'
DB_NAME='database_name'
DB_USER='database_user'
DB_PASSWORD='database_password'</code></pre>

  <h3>3. Install Dependencies</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

  <h3>4. Run Migrations</h3>
    <pre><code>python manage.py migrate</code></pre>

  <h3>5. (Optional) Create a Superuser</h3>
    <pre><code>python manage.py createsuperuser</code></pre>

  <h3>6. Start the Server</h3>
    <pre><code>python manage.py runserver</code></pre>

   <p>Access the project at: <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a></p>

  <h2>🌍 Current Endpoints (Under development)</h2>

  <h3>🔹 OCR (Text Extraction)</h3>
    <table>
        <tr>
            <th>Method</th>
            <th>Endpoint</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>POST</td>
            <td>/ocr/extract-text/</td>
            <td>Sends an image and receives the extracted text.</td>
        </tr>
    </table>

  <h3>Example Response:</h3>
    <pre><code>{
  "text": "Extracted text from the image"
}</code></pre>

  <h2>🔮 Future Features</h2>
    <ul>
        <li>Integration with a React frontend for testing and real-world usage.</li>
        <li>Authentication using JWT and refresh token.</li>
        <li>Access control by user level (admin, regular user).</li>
        <li>History of processed images per user.</li>
        <li>Support for PDFs and multiple images.</li>
        <li>Modern interface with real-time feedback.</li>
    </ul>

  <h2>📩 Contact</h2>
    <p>If you have any questions or suggestions, feel free to reach out!</p>
    <p>📧 Email: <a href="mailto:kailanesarahpro@gmail.com">kailanesarahpro@gmail.com</a></p>
    <p>🔗 GitHub: <a href="https://github.com/kailanesarah">https://github.com/kailanesarah</a></p>

   <p>⭐ If you liked the project, please leave a star on the repository! 🚀</p>

</body>
</html>
