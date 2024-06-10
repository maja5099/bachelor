% for key, social_media in global_content['social_media']['unid'].items():
<a id="icon_hover" href="{{ social_media['link'] }}">
  <div id="icon_small">
    <!-- prettier-ignore -->
    % include(f'{social_media["icon"]}')
  </div>
</a>
% end
