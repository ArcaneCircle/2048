# 2048 [![CI](https://github.com/webxdc/2048/actions/workflows/ci.yml/badge.svg)](https://github.com/webxdc/2048/actions/workflows/ci.yml) [![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

[2048](https://github.com/gabrielecirulli/2048) game ported to WebXDC.

<img width=200 src=https://user-images.githubusercontent.com/9800740/170771022-11536a6d-385c-4994-819c-458bc5dc04f1.png>

[Download .xdc from Release Assets](https://github.com/webxdc/2048.xdc/releases), attach to a Delta Chat group and share your 2048 highscores there!

## Contributing

### Installing Dependencies

After cloning this repo, install dependecies:

```
npm i
```

### Code format

```
npm run format:check
```

### Testing the app in the browser

To test your work in your browser (with hot reloading!) while developing:

```
npm run dev-mini
# Alternatively to test in a more advanced WebXDC emulator:
npm run dev
```

### Building

To package the WebXDC file:

```
npm run build
```

To package the WebXDC with developer tools inside to debug in Delta Chat, set the `NODE_ENV`
environment variable to "debug":

```
NODE_ENV=debug npm run build
```

The resulting optimized `.xdc` file is saved in `dist-xdc/` folder.

### Releasing

To automatically build and create a new GitHub release with the `.xdc` file:

```
git tag -a v1.0.1
git push origin v1.0.1
```
