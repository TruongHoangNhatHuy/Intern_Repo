// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  ssr: false,
  modules: [
    '@pinia/nuxt'
  ],
  runtimeConfig: {
    // The private keys which are only available within server-side
    // Keys within public, will be also exposed to the client-side
    public: {
      serverUrl: 'http://127.0.0.1:8000/api',
      oauthId: '88O0UVFkxiafTyTduL2xsJdcMZhbdYdR9QWFQrlr',
      oauthSecret: 'WlmWOb5VSTuYTsdcPaLSBlapclSF6GJSm6ubJNaIgccmJAziZ5C3m2YBRp7ldVvvxCQf4gfkSkAnXN8gC8VftHx88hlnK2PyrRgkloZHpW5DWGlKiDbt7EMDszFFRj3f',
    }
  },
  app: {
    head: {
      // import Bootstrap UI lib
      link: [
        {
          href: "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
          rel: "stylesheet",
          integrity:
            "sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN",
          crossorigin: "anonymous",
        },
      ],
      script: [
        {
          src: "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js",
          integrity:
            "sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL",
          crossorigin: "anonymous",
        },
      ],
    },
  },
})
