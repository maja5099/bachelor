<!DOCTYPE html>
<html lang="da">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Indsendte Beskeder</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="/static/script.js"></script>
</head>
<body>
  <div>
    <h1>Indsendte Beskeder</h1>
    <!-- prettier-ignore -->
    % if messages: 
    % for message in messages:
    <div>
      <h2>{{ message["first_name"] }} {{ message["last_name"] }}</h2>
      <h3>{{ message["website_name"] }} - {{ message["website_url"] }}</h3>
      <h4>Emne: {{ message["message_subject"] }}</h4>
      <p>Besked: {{ message["message_text"] }}</p>
      % if message['message_file']:
      <a href="{{ message['message_file'] }}" target="_blank">Se vedhæftede filer</a>
      % end
      <button data-message-id="{{ message['message_id'] }}" onclick="deleteMessage(this)">Slet Besked</button>
    </div>
    <!-- prettier-ignore -->
    % end 
    % else:
    <p>Ingen beskeder at vise.</p>
    % end
  </div>
</body>
</html>
