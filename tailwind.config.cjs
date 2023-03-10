/** @type {import('tailwindcss').Config} */
const colors = require("tailwindcss/colors.js");

module.exports = {
    content: ["index.html", "./src/**/*.{html,js,svelte,ts}"],
    theme: {
        extend: {
            width: {
                "3xl": "48rem",
            },
            minWidth: {
                "sm": "24rem",
            },
            maxWidth: {
                "s2": "16rem",
            },
            minHeight: {
                "8": "2rem",
            },
            colors: {
                primary: {
                    DEFAULT: "#DE0A82",
                    50: "#FFBCD7",
                    100: "#FF91CF",
                    200: "#F76CBB",
                    300: "#EF49A7",
                    400: "#E62994",
                    500: "#DE0A82",
                    600: "#AF176D",
                    700: "#801C55",
                    800: "#511939",
                    900: "#220E19"
                },
                gray: colors.stone
            }
        }
    },
    plugins: []
}
