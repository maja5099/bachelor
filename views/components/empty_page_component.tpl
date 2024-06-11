<div class="space-y-8">
  <div class="space-y-2">
    <p id="decorative_header">
      {{ subheader }}
    </p>
    <h2 class="capitalize">{{ header }}</h2>
  </div>
  <div>
    <div id="content_box_styling">
      <div id="content_box_header_styling">
        <p id="content_box_header_text">{{ box_header }}</p>
      </div>
      <div class="flex flex-col gap-10 p-6 text-unidPurple">
        <div class="justify-center items-center py-8 lg:py-10 text-center">
          <p class="text-sm font-bold">
            {{ global_content["empty_page"]["header_text"] }}
          </p>
          <p class="text-sm">
            {{ global_content["empty_page"]["subheader_text"] }}
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
