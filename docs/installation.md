# Installation and rollback

English | [简体中文](installation.zh-CN.md)

For the Nikon COOLPIX P7000 only. Before the first installation, update the camera to [official firmware 1.2](https://downloadcenter.nikonimglib.com/en/download/fw/45.html). If the camera already has stock firmware 1.2, do not repeat that step. This project uses the same SD-card-root `firmware` folder structure described by Nikon.

## Copy to the SD card

Download and extract `P7000-v3.4.3-SD.zip`. **Drag the entire firmware folder to the root of the SD card**:

```text
SD card root/
└── firmware/
    └── firmware.bin
```

Do not copy the README, research files or source code to the card. Keep the firmware filename unchanged, and do not put an extra P7000-v3.4.3-SD or project folder above `firmware`. Back up existing photographs before copying. If the card already contains a firmware folder, save the old firmware on the computer first to avoid mixing versions.

## Update the camera

Use a sufficiently charged battery. Insert the card while the camera is off, turn it on, then select **Set up → Firmware version → Update** and follow the on-screen instructions. During the update, do not operate the controls, switch off the camera or remove the battery/card. When instructed, shut down normally, remove the card and turn the camera on again.

The camera will still report **1.2**; this does not indicate a failed update. Project numbers such as v3.4.3 distinguish extension releases. There is no need to install historical project releases in sequence: use this complete image on the official 1.2 baseline.

Initial checks include NRW+JPEG in the SCN image-quality menu, two-axis WB adjustment of ±6, and the battery column to the left of the virtual-horizon column in Photo info. Final behavior still needs acceptance testing on the camera.

## Rollback

The complete research package includes full V3.4.2 and V3.3 rollback images. Take the firmware folder from the chosen version and use the same SD update procedure. Do not mix files from different versions.

V3.4.3 uses the P7C4 tag in the same independent 12-byte record. Earlier releases do not recognize this tag, so shared SCN adjustments may return to safe defaults after rollback and need to be set again. Ordinary-mode settings, U modes and calibration storage have not been repurposed. These rollback images are for cameras that can still enter the normal update menu; they are not a verified recovery method for a camera that will not start.

Current firmware SHA-256: `b147246ded1d43ff365a9e31f37565ff43676e4dc23e229946edb73e091040de`. On macOS/Linux, run `shasum -a 256 firmware/firmware.bin`. In Windows PowerShell, run `Get-FileHash firmware/firmware.bin -Algorithm SHA256`.
