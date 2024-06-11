<div
  class="w-full h-fit sticky top-44 bg-unidLightBlue rounded-lg p-6 space-y-4"
>
  <!-- prettier-ignore -->
  % if user and "user_role_id" in user:
    % if user["user_role_id"] == 1:
      % for customer_profile_menu in profile_content["customer_specific_content"]["customer_profile_menu"]:
  <button
    class="menu_button secondary_button w-full flex cursor-pointer"
    data-template="{{ customer_profile_menu['template'] }}"
  >
    <div class="h-6 w-6">
      <!-- prettier-ignore -->
      % include(f'{customer_profile_menu["icon"]}')
    </div>
    <p class="font-bold">{{ customer_profile_menu["text"] }}</p>
  </button>
  % end
  <!-- prettier-ignore -->
  % elif user["user_role_id"] == 2:
      % for admin_profile_menu in profile_content["admin_specific_content"]["admin_profile_menu"]:
  <button
    class="menu_button secondary_button w-full flex cursor-pointer"
    data-template="{{ admin_profile_menu['template'] }}"
  >
    <div class="h-6 w-6">
      <!-- prettier-ignore -->
      % include(f'{admin_profile_menu["icon"]}')
    </div>
    <p class="font-bold">{{ admin_profile_menu["text"] }}</p>
  </button>
  <!-- prettier-ignore -->
  % end 
  % end
  <div id="open_logout_pop_up">
    % include('components/profile/profile_logout')
  </div>
  % end
</div>
