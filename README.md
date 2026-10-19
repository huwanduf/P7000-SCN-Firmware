# P7000 SCN Firmware

**English** | [简体中文](README.zh-CN.md)

SCN scene-mode extensions for the **Nikon COOLPIX P7000**: NRW+JPEG, shared white-balance offsets and ISO, compatible My Menu controls, and a five-level battery indicator. The project retains each scene's native processing style.

Based on official firmware **1.2**. The current project release is **v3.4.3**; the camera still reports **1.2**. **P7000 only.**

## Downloads

| Package | Download |
|---|---|
| v3.4.3 SD update | [P7000-v3.4.3-SD.zip](https://github.com/huwanduf/P7000-SCN-Firmware/releases/download/v3.4.3/P7000-v3.4.3-SD.zip) |
| Reproducible source and research | [P7000-v3.4.3-research.zip](https://github.com/huwanduf/P7000-SCN-Firmware/releases/download/v3.4.3/P7000-v3.4.3-research.zip) |
| Checksums and earlier releases | [Releases](https://github.com/huwanduf/P7000-SCN-Firmware/releases) · [Changelog](CHANGELOG.md) |
| Current firmware image | [firmware/firmware.bin](firmware/firmware.bin) |

**v3.4.3 is the latest offline-validated candidate. Its new battery settings and power-cycle persistence still require validation on a camera.** Earlier v3.3 features received user testing; those results do not establish that this release has passed hardware acceptance.

## Install: official 1.2 first, then copy the firmware folder

1. **Before first installing this project, update the camera to Nikon's official 1.2.** Skip this step if it already runs official 1.2. [Official download and instructions](https://downloadcenter.nikonimglib.com/en/download/fw/45.html).
2. Download and extract the **SD update ZIP**. Drag the entire **`firmware` folder** to the **root of the SD card**.
3. The resulting path must be `SD card/firmware/firmware.bin`. Do not copy the ZIP or an extra enclosing project folder instead.
4. With a sufficiently charged battery, insert the card and open **Setup → Firmware version → Update**. Follow the camera's instructions and keep power connected throughout the update.
5. When finished, switch off as instructed, remove the card and restart. The displayed version remains **1.2**; identify project releases by their features and file checksums.

See the [installation and rollback guide](docs/installation.md). If you clone this repository or download its Source code ZIP, copy only the contained `firmware` folder to the SD card root. You do not need to install the project's intermediate releases in sequence.

## Current features

| Feature | v3.4.3 behavior |
|---|---|
| SCN NRW+JPEG | Enabled across SCN menu entries, subject to native image-size and special-capture compatibility checks |
| White balance | Shared **±6-step offsets on both axes**, added to each scene's native WB; remembered after normal shutdown; SCN opens the fine-tuning page directly |
| ISO | Shared valid ISO selections with persistence; the scene program determines minimum-shutter behavior |
| My Menu | Keeps the six registered slots and their order; selectively permits AF, metering, distortion control and Active D-Lighting under compatible scene conditions |
| Landscape flash | Adds Auto flash while retaining the scene's initialization rules |
| Battery indicator | Five display levels; **one red segment at critically low charge**; native warnings and shutdown protection retained |
| Battery settings | **Setup → Monitor settings → Photo info**; battery column is left of the virtual-horizon column; separate checkboxes for Show info and Hide info screens |

To show the battery in both shooting information screens, check **both** battery cells and select the original **Confirm** control. Leaving with MENU cancels unconfirmed edits. The current single-photo playback page follows the Show info checkbox.

The five levels group Nikon's native coarse estimates: **100 → 5**, **80/65 → 4**, **50 → 3**, **25 → 2**, **5/2 → 1 red segment**. This is a reading of the native cached battery estimate, not a fixed full-battery graphic. **It does not improve capacity-measurement precision.** Cache updates remain driven by native events; their actual interval has not been measured on the camera.

## Scene character and an older platform

SCN combines scene-specific color, exposure, noise processing and capture behavior. This project extends compatible controls within that processing chain instead of switching the whole camera into P/A/S/M.

SCN Picture Control therefore uses native scene defaults, minimum shutter follows the scene program, and burst capture retains each scene's original policy. To limit changes on this older platform, the firmware does not alter chip clocks, hardware initialization or calibration, and does not import unverified P7100 code. These are scope and stability choices; **not every unfinished feature has been proven to be limited by processing power**.

An earlier Picture Control entry produced a black screen and was withdrawn in v3.2.2. Expanded burst modes remain deferred because restoration of image quality, size and ISO is not sufficiently verified. Brief black screens or pauses when opening menus or returning to live view may remain; a system-wide speedup or elimination of those pauses has not been established. See [feature policy](docs/feature-policy.md) and the [version history](CHANGELOG.md).

## Validation and source

v3.4.3 passed four-section checksum, image-size, resource-boundary, complete-diff, bounded resource-loader replay and two independent rebuild checks, with **21,133 component test cases**. Offline checks cannot replace hardware testing or guarantee a risk-free update. [Validation scope](docs/validation.md) distinguishes computer-based evidence from user camera feedback.

Current `firmware.bin` SHA-256:

```text
b147246ded1d43ff365a9e31f37565ff43676e4dc23e229946edb73e091040de
```

Run `python3 tools/verify_firmware.py` to verify the repository image. The research asset contains the complete source and dependencies under `复现工程/`, with build entry `work/p7000-v3.4.3/build.py`, reproducibility instructions and earlier rollback images.

This is an unofficial research and feature-extension project, not a Nikon-certified update. Nikon firmware and trademarks remain the property of their rights holders; this repository does not relicense Nikon's original code as its own open-source work.
