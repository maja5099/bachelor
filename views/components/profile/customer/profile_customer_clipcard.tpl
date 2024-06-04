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
    % for card in clipcards:
% for clipcard_key, clipcard_value in pricing_default.items():
<div>
  <div class="flex justify-end">
    <div class="w-2/3 md:w-1/2 lg:w-2/3 bg-unidLightBlue border-unidLightBlue rounded-t-lg">
      <div class="flex gap-2 p-3 text-unidBeige items-center justify-center">
        <div class="w-5 h-5">
          % include(f"{clipcard_value['info']['discount_icon']}")
        </div>
        <p class="font-medium text-sm tracking-wider">
          {{ clipcard_value['info']['discount'] }}
        </p>
      </div>
    </div>
  </div>
  <div class="rounded-l-lg rounded-br-lg border-2 bg-unidBeige border-unidLightBlue flex flex-col">
    <div class="flex flex-col lg:flex-row justify-between gap-6">
      <div class="text-unidPurple space-y-1 p-6">
        <p class="text-sm tracking-widest title-font font-medium">
          {{ clipcard_value['info']['title'] }}
        </p>
        <h3>{{ card['clipcard_type_title'] }}</h3>
      </div>
    </div>
    <div class="border-b border-unidLightBlue mx-6"></div>
    <div class="p-6 space-y-6">
      <div class="space-y-2">
        % for point in clipcard_value['selling_points']:
        <div class="flex items-center gap-2 text-unidLightBlue">
          <div class="text-unidPurple w-5 h-5">
            <!-- prettier-ignore -->
            % include(f"{point['icon']}")
          </div>
          <p>{{ point['text'] }}</p>
        </div>
        % end
      </div>
      <div class="flex items-center justify-between gap-4">
        <p class="text-unidPurple text-base lg:text-lg">Pris</p>
        <div class="flex items-center gap-2">
          <p class="text-unidPurple text-right text-2xl xl:text-3xl font-saira font-bold">
            {{ card['clipcard_price'] }} DKK
          </p>
          <div class="flex flex-col text-xs text-unidPurple">
            <p>ekskl.</p>
            <p>moms</p>
          </div>
        </div>
      </div>
      <!-- prettier-ignore -->
      <button
        type="button"
        id="primary_button"
        class="buy-button"
        data-clipcard-type="{{ card['clipcard_type_title'] }}"
        data-clipcard-price="{{ card['clipcard_price'] }}">
        Køb nu
      </button>
    </div>
  </div>
</div>
% end
% end    
<script src="/static/script.js"></script>
</body>



