% for clipcard_key, clipcard in services_and_prices_content['prices_section']['pricings']['pricing_default'].items():
<div>
  <div class="flex justify-end">
    <div
      class="w-2/3 md:w-1/2 lg:w-2/3 bg-unidLightBlue border-unidLightBlue rounded-t-lg"
    >
      <div class="flex gap-2 p-3 text-unidBeige items-center justify-center">
        <div class="w-5 h-5">
          % include(global_content['ui_icons']['discount'])
        </div>
        <p class="font-medium text-sm tracking-wider">
          {{ clipcard["info"]["discount"] }}
        </p>
      </div>
    </div>
  </div>
  <div
    class="rounded-l-lg rounded-br-lg border-2 bg-unidBeige border-unidLightBlue flex flex-col"
  >
    <div class="flex flex-col lg:flex-row justify-between gap-6">
      <div class="text-unidPurple space-y-1 p-6">
        <p class="text-sm tracking-widest title-font font-medium">
          {{ clipcard["info"]["title"] }}
        </p>
        <h3>{{ clipcard["info"]["hours"] }}</h3>
      </div>
    </div>
    <div class="border-b border-unidLightBlue mx-6"></div>
    <div class="p-6 space-y-6">
      <div class="space-y-2">
        % for point in clipcard['selling_points']:
        <div class="flex items-center gap-2 text-unidLightBlue">
          <div class="text-unidPurple w-5 h-5">
            % include(global_content['ui_icons']['checkmark'])
          </div>
          <p>{{ point["text"] }}</p>
        </div>
        % end
      </div>
      <div class="flex items-center justify-between gap-4">
        <p class="text-unidPurple text-base lg:text-lg">Pris</p>
        <div class="flex items-center gap-2">
          <p
            class="text-unidPurple text-right text-2xl xl:text-3xl font-saira font-bold"
          >
          <!-- sadsdasd -->
            {{ clipcard["info"]["price"] }}
          </p>
          <div class="flex flex-col text-xs text-unidPurple">
            <p>ekskl.</p>
            <p>moms</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
% end
