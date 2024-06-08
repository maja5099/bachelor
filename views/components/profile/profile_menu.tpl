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
  </body>
</html>
