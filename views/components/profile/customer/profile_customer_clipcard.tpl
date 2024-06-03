<body>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    
 <h2>KLIPPEKORT</h2>
    <h1>Hvorfor købe et klippekort?</h1>
    <p>
      Lorem Ipsum is simply dummy text of the printing and typesetting industry.
      Lorem Ipsum has been the industry's standard dummy text ever since the
      1500s,. When an unknown printer took a galley of type and scrambled it to
      make a type specimen book. It has survived not only five centuries, but
      also the leap into electronic typesetting, remaining essentially
      unchanged. It was popularised in the 1960s with the release of Letraset
      sheets containing.
    </p>
    <div>
      % for card in clipcards:
      <h2>KLIPPEKORT</h2>
      <h3>{{ card['clipcard_type_title'] }}</h3>
      <h4>Pris: {{ card['clipcard_price'] }} kr</h4>

      <button
        type="button"
        class="buy-button"
        data-clipcard-type="{{ card['clipcard_type_title'] }}"
        data-clipcard-price="{{ card['clipcard_price'] }}">
        Køb nu
      </button>
      % end

<script src="/static/script.js"></script>
</body>