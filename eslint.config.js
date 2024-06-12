const globals = require("globals");
const pluginJs = require("@eslint/js");

export const eslintConfig = [
  { files: ["static/**/*.js"], languageOptions: { sourceType: "module" } },
  { languageOptions: { globals: globals.browser } },
  pluginJs.configs.recommended,
];
