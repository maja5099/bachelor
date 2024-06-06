<div
  class="w-full h-fit sticky top-44 bg-unidLightBlue rounded-lg p-6 space-y-4"
>
  <!-- prettier-ignore -->
  % if user and "user_role_id" in user:
    % if user["user_role_id"] == 1:
      % for section_profile_customer in section_profile_customer:
  <button
    class="secondary_button w-full flex cursor-pointer"
    data-template="{{ section_profile_customer['template'] }}"
  >
    <div class="h-6 w-6">
      <!-- prettier-ignore -->
      % include(f'{section_profile_customer["icon"]}')
    </div>
    <p class="font-bold">{{ section_profile_customer["text"] }}</p>
  </button>
  % end
  <!-- prettier-ignore -->
  % elif user["user_role_id"] == 2:
      % for section_profile_admin in section_profile_admin:
  <button
    class="secondary_button w-full flex cursor-pointer"
    data-template="{{ section_profile_admin['template'] }}"
  >
    <div class="h-6 w-6">
      <!-- prettier-ignore -->
      % include(f'{section_profile_admin["icon"]}')
    </div>
    <p class="font-bold">{{ section_profile_admin["text"] }}</p>
  </button>
  <!-- prettier-ignore -->
  % end 
  % end
  <div id="open_logout_pop_up">
    % include('components/profile/profile_logout')
  </div>
  % else:
  <p>Du skal være logget ind for at se denne side</p>
  % end
</div>
