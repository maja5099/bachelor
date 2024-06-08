<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- CSS -->
    <link rel="stylesheet" href="/app.css" />
    <!-- FONTS -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Saira:ital,wght@0,100..900;1,100..900&display=swap"
      rel="stylesheet"
    />
    <!-- FAVICONS -->
    <link
      rel="apple-touch-icon"
      sizes="180x180"
      href="/assets/favicon/apple-touch-icon.png"
    />
    <link
      rel="icon"
      type="image/png"
      sizes="32x32"
      href="/assets/favicon/favicon-32x32.png"
    />
    <link
      rel="icon"
      type="image/png"
      sizes="16x16"
      href="/assets/favicon/favicon-16x16.png"
    />
    <link
      rel="icon"
      type="image/png"
      sizes="192x192"
      href="/assets/favicon/android-chrome-192x192.png"
    />
    <link
      rel="icon"
      type="image/png"
      sizes="512x512"
      href="/assets/favicon/android-chrome-512x512.png"
    />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  </head>
  <body>
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
                  Her vil du kunne få et overblik over timerne på dit
                  klippekort.
                </p>
                <p class="text-sm">
                  Klik på 'Klippekort' i menuen, og vælge det klippekort, der
                  passer til dig!
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
  </body>
</html>
