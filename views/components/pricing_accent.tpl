% for clipcard_key, clipcard_value in pricing_accent.items():
<div class="col-span-1 md:col-span-2 xl:col-span-1">
  <div class="flex justify-end">
    <div class="w-2/3 md:w-1/3 xl:w-2/3 bg-unidPurple text-white rounded-t-lg">
      <div class="flex gap-3 p-3 items-center justify-center">
        <div class="w-6 h-6">
          % include(f'{clipcard_value['info']['discount_icon']}')
        </div>
        <p class="font-medium tracking-wider text-base">
          {{ clipcard_value['info']['discount'] }}
        </p>
      </div>
    </div>
  </div>
  <div
    class="rounded-l-lg rounded-br-lg border-2 bg-unidBeige border-unidBlue flex flex-col"
  >
    <div class="bg-unidBlue flex flex-col lg:flex-row justify-between gap-6">
      <div class="text-white space-y-1 p-6">
        <p class="text-sm tracking-widest title-font font-medium">
          {{ clipcard_value['info']['title'] }}
        </p>
        <h3 class="text-white">{{ clipcard_value['info']['hours'] }}</h3>
      </div>
    </div>
    <div class="p-6 space-y-6">
      <div class="space-y-2">
        % for point in clipcard_value['selling_points']:
        <div class="flex items-center gap-2 text-unidLightBlue">
          <div class="text-unidPurple w-5 h-5">
            <!-- prettier-ignore -->
            % include(f'{point['icon']}')
          </div>
          <p>{{ point['text'] }}</p>
        </div>
        % end
      </div>
      <div class="flex items-center justify-between gap-4">
        <p class="text-unidPurple text-base lg:text-lg">Pris</p>
        <div class="flex items-center gap-2">
          <p
            class="text-unidBlue text-right text-2xl xl:text-3xl font-saira font-bold"
          >
            {{ clipcard_value['info']['price'] }}
          </p>
          <div class="flex flex-col text-xs text-unidPurple">
            <p>ekskl.</p>
            <p>moms</p>
          </div>
        </div>
      </div>
      <!-- prettier-ignore -->
      % include('utilities/buttons/primary_button', type='button', link='/', button_text='Køb nu')
    </div>
  </div>
</div>
% end
