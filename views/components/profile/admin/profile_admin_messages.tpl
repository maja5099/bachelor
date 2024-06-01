<div>
  <h1>Indsendte Beskeder TESSSSTTTTT</h1>
  <!-- prettier-ignore -->
  % if message: 
  % for message in messages:
  <div style="background-color: gainsboro; margin-bottom: 10px">
    <h2>{{ message["first_name"] }} {{ message["last_name"] }}</h2>
    <h3>{{ message["website_name"] }} - {{ message["website_url"] }}</h3>
    <h4>Emne: {{ message["message_subject"] }}</h4>
    <p>Besked: {{ message["message_text"] }}</p>
    % if message['message_file']:
    <a href="{{ message['message_file'] }}" target="_blank"
      >Se vedhæftede filer</a
    >
    % end
    <button
      data-message-id="{{ message['message_id'] }}"
      onclick="deleteMessage(this)"
    >
      Slet Besked
    </button>
  </div>
  <!-- prettier-ignore -->
  % end 
  % else:
  <p>Ingen beskeder at vise.</p>
  % end
</div>
