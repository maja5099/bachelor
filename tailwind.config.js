/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: [
    "./views/**/*.*",
    "./assets/**/*.*",
    "./views/components/**/*.*",
    "./views/components/profile/**/*.*",
    "./views/components/profile/customer/**/*.*",
    "./views/components/profile/admin/**/*.*",
    "./views/elements/**/*.*",
    "./views/sections/**/*.*",
    "./views/utilities/**/*.*",
    "./views/utilities/buttons/**/*.*",
  ],
  theme: {
    extend: {
      colors: {
        unidBlue: "#1D1B6E",
        unidLightBlue: "#A0B4D3",
        unidLightBlueHover: "#AEBFDA",
        unidPurple: "#59437B",
        unidLightPurple: "#E4CBE5",
        unidYellow: "#F7F0E6",
        unidPink: "#F5DBE3",
        unidBeige: "#F2EBED",
      },
      fontFamily: {
        saira: "'Saira', sans-serif",
        montserrat: "'Montserrat', sans-serif",
      },
      backgroundImage: {
        wave: "url('/assets/graphics/wave.svg')",
      },
    },
    plugins: [],
  },
};
