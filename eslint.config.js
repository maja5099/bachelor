import globals from "globals";
import pluginJs from "@eslint/js";

export default [
  { files: ["static/**/*.js"], languageOptions: { sourceType: "module" } },
  { languageOptions: { globals: globals.browser } },
  pluginJs.configs.recommended,
];
