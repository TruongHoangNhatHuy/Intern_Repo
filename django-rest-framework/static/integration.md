## Integrate Nuxt app into Django

- config Vite options in `nuxt.config.js`
- build Nuxt app: run terminal `npx nuxt generate`
- copy from Nuxt `./.nuxt/dist/` to Django `./static/`
- copy from Nuxt `./.output/public/_nuxt/builds/` to Django `./static/dist/client/_nuxt/`
- config django-vite in `settings.py`: [Guide](https://github.com/MrBin99/django-vite?tab=readme-ov-file#usage)
- edit Django templates `./templates/index.html`