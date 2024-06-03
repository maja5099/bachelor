<body>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="/static/script.js"></script>
    
    <h1>Aktive Klippekort</h1>

    % for clipcard in active_clipcards:
    <div id="clipcard_{{ clipcard['clipcard_id'] }}">
      <h2>{{ clipcard['first_name'] }} {{ clipcard['last_name'] }} - {{ clipcard['website_url'] }}</h2>
      <p>{{ clipcard['remaining_time_text'] }}</p>

      <div>
        <h3>Brugeroplysninger</h3>
        <p>Navn: {{ clipcard['first_name'] }} {{ clipcard['last_name'] }}</p>
        <p>Brugernavn: {{ clipcard['username'] }}</p>
        <p>Email: {{ clipcard['email'] }}</p>
      </div>

      <div>
        <h3>Website</h3>
        <p>Navn: {{ clipcard['website_name'] }}</p>
        <p>URL: {{ clipcard['website_url'] }}</p>
      </div>

      <div>
        <h3>Klippekortoplysninger</h3>
        <p>Klippekort ID: {{ clipcard['clipcard_id'] }}</p>
        <p>Klippekorttype: {{ clipcard['clipcard_type_title'] }}</p>
      </div>

      <div>
        <h3>Timeoverblik</h3>
        <p>Tid brugt: {{ clipcard['time_used_text'] }}</p>
        <p>Tid tilbage: {{ clipcard['remaining_time_text'] }}</p>
      </div>

      <button
        type="button"
        class="delete-button"
        data-clipcard-id="{{ clipcard['clipcard_id'] }}"
      >
        Slet klippekort
      </button>
    </div>
    % end

    <h1>Timeregistrering</h1>
    <form
      id="taskForm"
      action="/submit_task"
      method="post"
    >
      <label for="customer">Kunde:</label>
      <select id="customer" name="customer">
        % for customer in active_customers:
        <option value="{{customer['user_id']}}">
          {{customer['first_name']}} {{customer['last_name']}}
        </option>
        % end
      </select>
      <br />
      <label for="title">Opgavetitel:</label>
      <textarea id="title" name="title"></textarea>
      <br />
      <label for="description">Opgavebeskrivelse:</label>
      <textarea id="description" name="description"></textarea>
      <br />
      <label for="hours">Tid brugt:</label>
      <input type="number" id="hours" name="hours" min="0" step="1" value="0" />
      timer
      <input
        type="number"
        id="minutes"
        name="minutes"
        min="0"
        max="59"
        step="1"
        value="0"
      />
      minutter
      <br />
      <input type="submit" value="Registrer" />
    </form>

    <div id="responseMessage"></div>
</body>