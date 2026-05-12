# Model Viewer

Standalone OpenGL 3D viewer for GTA III / VC / SA DFF model files.

Part of the [IMG Factory 1.6](https://github.com/X-Seti/Img-Factory-1.6) modding suite.

## Features
- OpenGL hardware rendering (wire/solid/textured)
- SA vehicle paint system (primary/secondary colour slots)
- Assembly mode with wheels.DFF support
- Auto-load shared TXDs (vehicle.txd, gta3.img scan)
- Carcols.dat colour picker
- IMG file browser with double-click to preview

## Requirements
```
pip install PyQt6 PyOpenGL
```

## Standalone Usage
```bash
./model_viewer.py [file.dff] [file.txd]
```
