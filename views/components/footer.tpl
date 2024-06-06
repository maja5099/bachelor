<footer class="text-white text-sm bg-unidLightBlue">
  <div
    class="width_big mx-auto gap-6 py-10 flex justify-between items-center flex-col lg:flex-row"
  >
    <!-- LOGO -->
    % if user:
    <a href="/">
      <img
        class="w-16"
        src="/assets/logos/{{ unid_logo['secondary_logo'] }}"
        alt="{{ unid_logo['logo_alt'] }}"
      />
    </a>
    % else:
    <a href="/">
      <img
        class="w-16"
        src="/assets/logos/{{ unid_logo['primary_logo'] }}"
        alt="{{ unid_logo['logo_alt'] }}"
      />
    </a>
    % end
    <!-- FOOTER INFO -->
    <div
      class="text-xs flex-col cursor-default flex lg:flex-row justify-center text-center gap-2 lg:gap-6"
    >
      % for footer_info in footer_info:
      <p>{{ footer_info }}</p>
      % end
    </div>
    <!-- SOME -->
    <div class="flex items-center text-center justify-center gap-2">
      % include('elements/social_media')
    </div>
  </div>
</footer>
