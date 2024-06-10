% for clipcard_key, clipcard in services_and_prices_content['prices_section']['pricings']['pricing_accent'].items():
<div class="col-span-1 md:col-span-2 xl:col-span-1">
  <div class="flex justify-end">
    <div
      class="w-2/3 md:w-1/3 xl:w-2/3 bg-unidLightPurple text-unidPurple rounded-t-lg"
    >
      <div class="flex gap-3 p-3 items-center justify-center">
        <div class="w-6 h-6">
          % include(global_content['ui_icons']['discount_full'])
        </div>
        <p class="font-medium tracking-wider text-base">
          {{ clipcard["info"]["discount"] }}
        </p>
      </div>
    </div>
  </div>
  <div
    class="rounded-l-lg rounded-br-lg border-2 bg-unidBeige border-unidPurple flex flex-col"
  >
    <div class="bg-unidPurple flex flex-col lg:flex-row justify-between gap-6">
      <div class="text-white space-y-1 p-6">
        <p class="text-sm tracking-widest title-font font-medium">
          {{ clipcard["info"]["title"] }}
        </p>
        <h3 class="text-white">{{ clipcard["info"]["hours"] }}</h3>
      </div>
    </div>
    <div class="p-6 space-y-6">
      <div class="space-y-2">
        % for point in clipcard['selling_points']:
        <div class="flex items-center gap-2 text-unidLightBlue">
          <div class="text-unidPurple w-5 h-5">
            % include(global_content['ui_icons']['checkmark_full'])
          </div>
          <p>{{ point["text"] }}</p>
        </div>
        % end
      </div>
      <div class="flex items-center justify-between gap-4">
        <p class="text-unidPurple text-base lg:text-lg">Pris</p>
        <div class="flex items-center gap-2">
          <p
            class="text-unidBlue text-right text-2xl xl:text-3xl font-saira font-bold"
          >
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
