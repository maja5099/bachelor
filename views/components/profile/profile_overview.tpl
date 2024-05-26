<div class="grid gap-10 md:gap-8">
  <div
    class="w-full h-full bg-unidLightBlue rounded-lg text-white justify-between xl:flex items-center p-6 space-y-2"
  >
    <!-- prettier-ignore -->
    % if "user_roles_user_role_id" in user:
        % if user["user_roles_user_role_id"] == 1:
    <p class="font-bold text-lg">
      Velkommen, {{ first_name }} {{ last_name }}!
    </p>
    <div class="flex gap-1 text-sm">
      <p>Du har</p>
      <p class="font-bold">1 aktivt</p>
      <p>klippekort A</p>
    </div>
    % elif user["user_roles_user_role_id"] == 2:
    <p class="font-bold text-lg">
      Velkommen, {{ first_name }} {{ last_name }}!
    </p>
    <div class="flex gap-1 text-sm">
      <p>Du er logget ind som</p>
      <p class="font-bold">admin</p>
    </div>
    % end
    <!-- prettier-ignore -->
    % end
  </div>

  <div class="grid lg:grid-cols-2 gap-8">
    <!-- prettier-ignore -->
    % if "user_roles_user_role_id" in user:
        % if user["user_roles_user_role_id"] == 1:
            % include('components/profile/profile_box', box_icon=ui_icons['hourglass_icon'], box_title='Tid tilbage', box_content_big='123', box_content_medium='timer', box_content_small='123', box_content_xsmall='minutter')
            % include('components/profile/profile_box', box_icon=ui_icons['stop_watch_icon'], box_title='Tid brugt', box_content_big='123', box_content_medium='timer', box_content_small='123', box_content_xsmall='minutter')
        % elif user["user_roles_user_role_id"] == 2:
            % include('components/profile/profile_box', box_icon=ui_icons['open_folder_icon'], box_title='Åbne klippekort', box_content_big='123', box_content_medium='klippekort', box_content_small='', box_content_xsmall='')
            % include('components/profile/profile_box', box_icon=ui_icons['closed_folder_icon'], box_title='Lukkede klippekort', box_content_big='123', box_content_medium='klippekort', box_content_small='', box_content_xsmall='')
        % end
      % end
  </div>
</div>