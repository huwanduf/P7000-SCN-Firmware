# v3.2.2 · Native scene style and shared controls

English | [简体中文](README.zh-CN.md)

## v3.2.2 — Native scene style and shared controls

**Historical archive — not the latest firmware.** [Current v3.4.3 candidate](https://github.com/huwanduf/P7000-SCN-Firmware/releases/tag/v3.4.3). This release was separated from the latest download page; its firmware and original SD ZIP are unchanged.

### Compatibility and included features

- **Camera:** Nikon COOLPIX P7000 only. Install official Nikon **1.2** first; the camera continues to report 1.2.
- **Included:** Includes all-SCN NRW+JPEG, shared scene-native WB offsets of ±2 on both axes, shared ISO with shutdown persistence, and compatible AF, metering, distortion control and Active D-Lighting through My Menu.
- **Suitable use:** For shared WB/ISO and compatible My Menu controls while retaining native scene Picture Control.
- **Retained limits:** SCN Picture Control stays disabled and uses native scene values; minimum shutter and burst behavior follow the scene. No ±6 WB, landscape Auto flash or custom battery display. Menu/live-view pauses remain.
- **Hardware feedback:** The user described the build as fully usable. This is user feedback, not independent testing of every scene and combination.

### Install

Download **`P7000-v3.2.2-SD.zip`**, extract it, and drag the entire **firmware** folder to the SD card root: `firmware/firmware.bin`. Use a charged battery, open Setup → Firmware version → Update, and keep power connected. Intermediate project versions do not need to be installed in order.

The tag's automatic Source code archive also contains this version's matching firmware and version-specific instructions, not the v3.4.3 image. It is a new archival tag, not a reconstruction of the original development Git history. The ongoing research/source bundle remains on the current release page.

Firmware SHA-256: `f69fb7f30de084eee24d4c6a98ae51727192f98af1cad286bba81e26f942cdd6`

SD ZIP SHA-256: `bf8713256bc345865ac55cdc7fc49239b8b303050db56a82f9cae89617b7ad57`

