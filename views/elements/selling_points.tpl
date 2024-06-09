% for selling_point in global_content['header']['header_bar']['selling_points']:
<li
  class="flex items-center cursor-default text-center text-unidPurple justify-center gap-2"
>
  <div id="icon_small" class="fill-unidPurple">
    <!-- prettier-ignore -->
    % include(f'{selling_point["icon"]}')
  </div>
  <p id="selling_point">{{ selling_point["text"] }}</p>
</li>
% end
