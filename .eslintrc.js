module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  extends: "eslint:recommended",
  parserOptions: {
    ecmaVersion: 12,
    sourceType: "module",
  },
  rules: {
    "no-unused-vars": "warn",
    indent: ["error", 2],
    quotes: ["error", "single"],
    semi: ["error", "always"],
    "comma-dangle": ["error", "always-multiline"],
    "no-trailing-spaces": "error",
    "comma-spacing": "error",
    "brace-style": "error",
    "no-multi-spaces": "error",
    "arrow-spacing": "error",
    "no-multiple-empty-lines": "error",
    "no-var": "error",
    "prefer-const": "error",
  },
  globals: {
    $: true,
  },
};
