<div id="content_box_styling">
  <div class="bg-unidLightBlue p-6 items-center">
    <div
      class="flex md:flex-col lg:flex-row gap-4 md:gap-2 lg:gap-4 items-center justify-center"
    >
      <div id="icon_medium" class="fill-unidPurple">
        % include(f'{box_icon}')
      </div>
      <p id="content_box_header_text">{{ box_title }}</p>
    </div>
  </div>
  <div class="flex flex-col gap-4 p-6 items-center">
    <div class="text-unidPurple flex gap-2 items-center">
      <p class="font-saira font-bold text-6xl md:text-5xl lg:text-6xl">
        {{ box_content_big }}
      </p>
      <p class="text-xl">{{ box_content_medium }}</p>
    </div>
    <div class="text-unidPurple flex gap-2 items-center">
      <p class="font-saira font-bold text-4xl md:text-2xl lg:text-4xl">
        {{ box_content_small }}
      </p>
      <p class="text-lg md:text-base lg:text-lg">{{ box_content_xsmall }}</p>
    </div>
  </div>
</div>
