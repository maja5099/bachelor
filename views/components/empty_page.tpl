<div class="space-y-8">
  <div class="space-y-2">
    <p class="text-md tracking-widest text-unidPurple uppercase">
      {{ subheader }}
    </p>
    <h2 class="capitalize">{{ header }}</h2>
  </div>
  <div>
    <div
      class="w-full h-full rounded-lg text-white justify-center items-center bg-unidYellow border-2 border-unidLightBlue"
    >
      <div class="bg-unidLightBlue text-center p-6 items-center">
        <p class="font-bold text-lg capitalize">{{ box_header }}</p>
      </div>
      <div class="flex flex-col gap-10 p-6 text-unidPurple">
        <div class="justify-center items-center py-8 lg:py-10 text-center">
          <p class="text-sm font-bold">{{ global_content["empty_page"]["header_text"] }}</p>
          <p class="text-sm">
            {{ global_content["empty_page"]["subheader_text"] }}
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
