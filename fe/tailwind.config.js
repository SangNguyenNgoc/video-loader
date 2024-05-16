/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors :{
        primary:"#0064DF",
        secondary:"#F4F5FA"
      },
      boxShadow:{
        "main":"0 13px 34px 0 rgba(60,111,139,.1)"
      }
    },
  },
  plugins: [
    
  ],
}

