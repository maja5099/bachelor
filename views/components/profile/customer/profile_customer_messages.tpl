<body>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="/static/script.js"></script>
    <h2>KONTAKT</h2>
    <h1>Har du noget der skal rettes eller laves på dit website?</h1>
    <form id="contactForm" enctype="multipart/form-data">
        <div>
            <label for="subject">Emne:</label>
            <input type="text" id="subject" name="subject" required />
        </div>
        <div>
            <label for="message">Besked:</label>
            <textarea id="message" name="message" required></textarea>
        </div>
        <div>
            <label for="file">Upload fil:</label>
            <input type="file" id="file" name="file" accept=".png, .jpg, .jpeg" />
        </div>
        <button type="button" id="sendMessageButton">Send</button>
        <div id="messageSent" style="display: none"></div>
    </form>
</body>
