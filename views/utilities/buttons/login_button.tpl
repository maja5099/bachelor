<div>
  <!-- DESKTOP -->
  <button
    id="login_button"
    onclick="location.href='{{ link }}'"
    class="hidden lg:flex"
  >
    <div id="icon_small">
      <!-- prettier-ignore -->
      % if user and "user_role_id" in user:
        % if user["user_role_id"] == 1:
          % include(global_content['ui_icons']['user'])
        % elif user["user_role_id"] == 2:
          % include(global_content['ui_icons']['admin'])
        % end
      % else:
        % include(global_content['ui_icons']['user'])
      % end
    </div>
    {{ button_text }}
  </button>

  <!-- MOBILE -->
  <div class="flex lg:hidden">
    <button id="icon_hover" onclick="location.href='{{ link }}'">
      <div id="icon_small">
        <!-- prettier-ignore -->
        % if user and "user_role_id" in user:
        % if user["user_role_id"] == 1:
          % include(global_content['ui_icons']['user'])
        % elif user["user_role_id"] == 2:
          % include(global_content['ui_icons']['admin'])
        % end
        % else:
          % include(global_content['ui_icons']['user'])
        % end
      </div>
    </button>
  </div>
</div>
