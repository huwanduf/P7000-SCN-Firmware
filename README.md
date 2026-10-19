# v3.3 · WB ±6 and Landscape Auto flash

English | [简体中文](README.zh-CN.md)

## v3.3 — WB ±6 and Landscape Auto flash

**Historical archive — not the latest firmware.** [Current v3.4.3 candidate](https://github.com/huwanduf/P7000-SCN-Firmware/releases/tag/v3.4.3). This release was separated from the latest download page; its firmware and original SD ZIP are unchanged.

### Compatibility and included features

- **Camera:** Nikon COOLPIX P7000 only. Install official Nikon **1.2** first; the camera continues to report 1.2.
- **Included:** Builds on v3.2.2 with shared scene-native WB offsets of ±6 on both axes, migration of older WB/ISO records, and Auto/Off flash choices in Landscape. Existing RAW+JPEG, ISO persistence and compatible My Menu controls remain.
- **Suitable use:** For the expanded SCN controls without the later custom battery UI.
- **Retained limits:** Landscape still initializes with flash off; pop up the flash and select Auto when needed. Picture Control/minimum shutter/burst retain scene policies. No five-level battery settings. Blackouts and speed improvements have not been established.
- **Hardware feedback:** The user reported that the main features worked very well apart from lag. No independent per-feature shooting report is available.

### Install

Download **`P7000-v3.3-SD.zip`**, extract it, and drag the entire **firmware** folder to the SD card root: `firmware/firmware.bin`. Use a charged battery, open Setup → Firmware version → Update, and keep power connected. Intermediate project versions do not need to be installed in order.

The tag's automatic Source code archive also contains this version's matching firmware and version-specific instructions, not the v3.4.3 image. It is a new archival tag, not a reconstruction of the original development Git history. The ongoing research/source bundle remains on the current release page.

Firmware SHA-256: `db946841a6ded0be1ffce830bc2fb88868cd109c58931f7c5af971252ea0a4b2`

SD ZIP SHA-256: `bd676c7e1c9069d4908097bfd646cece348045f8d80907d6cb5139a2f82f4d88`

