<div class="grid gap-10 md:gap-8">
  <div
    class="w-full h-full bg-unidLightBlue rounded-lg text-white justify-between xl:flex items-center p-6 space-y-2"
  >
    <!-- prettier-ignore -->
    % if "user_role_id" in user:
      % if user["user_role_id"] == 1:
    <p class="font-bold text-lg">
      Velkommen, {{ first_name }} {{ last_name }}!
    </p>
    % if current_user and not current_user.get('has_active_clipcard'):
    <div class="flex gap-1 text-sm">
      <p>Du har ikke noget klippekort endnu</p>
    </div>
    % else:
    <div class="flex gap-1 text-sm">
      <p>Du har</p>
      <p class="font-bold">1 aktivt</p>
      <p>klippekort</p>
    </div>
    <!-- prettier-ignore -->
    % end
      % elif user["user_role_id"] == 2:
    <p class="font-bold text-lg">
      Velkommen, {{ first_name }} {{ last_name }}!
    </p>
    <div class="flex gap-1 text-sm">
      <p>Du er logget ind som</p>
      <p class="font-bold">admin</p>
    </div>
    <!-- prettier-ignore -->
    % end
    % end
  </div>
  <!-- prettier-ignore -->
  % if user["user_role_id"] == 1: 
  % if current_user and not current_user.get('has_active_clipcard') and "user_role_id" in user:
  <div class="space-y-8">
    <div>
      <div
        class="w-full h-full rounded-lg text-white justify-center items-center bg-unidYellow border-2 border-unidLightBlue"
      >
        <div class="bg-unidLightBlue text-center p-6 items-center">
          <p class="font-bold text-lg capitalize">Klippekort</p>
        </div>
        <div class="flex flex-col gap-10 p-6 text-unidPurple">
          <div
            class="justify-center space-y-1 items-center py-8 lg:py-10 text-center"
          >
            <p class="text-sm font-bold">
              Hov, du har ikke et klippekort endnu...
            </p>
            <p class="text-sm">
              Her vil du kunne få et overblik over timerne på dit klippekort.
            </p>
            <p class="text-sm">
              Klik på 'Klippekort' i menuen, og vælge det klippekort, der passer
              til dig!
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
  % else:
  <div class="grid lg:grid-cols-2 gap-8">
    <!-- prettier-ignore -->
    % include('components/profile/profile_box', box_icon=ui_icons['hourglass_icon'], box_title='Tid tilbage', box_content_big=remaining_hours, box_content_medium='timer', box_content_small=remaining_minutes, box_content_xsmall='minutter')
    % include('components/profile/profile_box', box_icon=ui_icons['stop_watch_icon'], box_title='Tid brugt', box_content_big=time_used_hours, box_content_medium='timer', box_content_small=time_used_minutes, box_content_xsmall='minutter')
  </div>
  <!-- prettier-ignore -->
  % end
  % end

  <div class="grid lg:grid-cols-2 gap-8">
    <!-- prettier-ignore -->
    % if "user_role_id" in user: 
      % if  user["user_role_id"] == 2: 
      % include('components/profile/profile_box', box_icon=ui_icons['open_folder_icon'], box_title='Åbne klippekort', box_content_big=active_clipcards_count, box_content_medium='klippekort', box_content_small='', box_content_xsmall='')
      % include('components/profile/profile_box', box_icon=ui_icons['closed_folder_icon'], box_title='Lukkede klippekort', box_content_big=inactive_clipcards_count, box_content_medium='klippekort', box_content_small='', box_content_xsmall='') 
    % end 
  % end
  </div>
</div>
