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
    "no-unused-vars": "warn", // Vis advarsler for uudnyttede variabler
    indent: ["error", 2], // Vis fejl, hvis der ikke er to mellemrum for indrykning
    quotes: ["error", "single"], // Vis fejl, hvis der ikke bruges enkeltcitationstegn
    semi: ["error", "always"], // Vis fejl, hvis der mangler semikolon
    "comma-dangle": ["error", "always-multiline"], // Vis fejl, hvis der mangler komma ved multiline statements
    "no-trailing-spaces": "error", // Vis fejl, hvis der er trailing spaces
    "comma-spacing": "error", // Vis fejl, hvis der er fejl i komma-spacing
    "brace-style": "error", // Vis fejl, hvis der er fejl i brace style
    "no-multi-spaces": "error", // Vis fejl, hvis der er multiple spaces
    "arrow-spacing": "error", // Vis fejl, hvis der er fejl i arrow spacing
    "no-multiple-empty-lines": "error", // Vis fejl, hvis der er multiple empty lines
    "no-var": "error", // Vis fejl, hvis var bruges i stedet for let/const
    "prefer-const": "error", // Vis fejl, hvis der bruges let i stedet for const, når variablen ikke ændres
  },
};
