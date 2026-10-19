# Changelog

English | [简体中文](CHANGELOG.zh-CN.md)

These are project release numbers; the camera's displayed firmware version remains **1.2** throughout. V1/V2 are historical labels assigned to the first two previously unnamed packages, not changes to the camera version.

| Project release | Main changes | Trade-offs and known issues | Hardware evidence |
|---|---|---|---|
| v3.4.3 · Five-bar battery and native-style info menu | Battery column to the left of the virtual horizon; independent switches for Show info/Hide info views; five bars, with one red bar at native levels 5/2; P7C4 migration. | Still reads the factory seven-level cache, without greater measurement precision. The current single-photo playback page uses only the Show info row. New UI, callbacks and shutdown persistence await hardware acceptance. | 21,133 component cases, integrated checks and two reconstruction paths passed. No hardware-pass feedback for this release yet. |
| v3.4.2 · Native-style checkbox | Removed the Fn dependency; added a focusable checkbox at the bottom of Photo info and a diagnostic cache-value title. | The user then requested integration into the original grid. 100/80 still shared the full-bar state; cached 100 is not an exact measurement of remaining capacity. | Subsequent interface photographs and layout feedback; no complete hardware acceptance of the new switch. |
| v3.4.1 · Three-bar battery graphic | Replaced percentages with a three-bar graphic, retaining the full-level display switch. | The user confirmed that the graphic worked, but the Fn switch did not and its label had inconsistent typography. V3.4.2 redesigned the setting entry. | Graphic confirmed by the user; Fn switch failed. |
| v3.4 · Factory-estimated battery display | Added seven-level factory percentage estimates in live view and single-photo playback, a full-level display switch, and independent-record migration. | User photographs showed clipped percentage text. The physical Fn switch was not verified and was later redesigned. The value remained a factory cache reading, not a 1% measurement. | Hardware photographs exist; the display issue cannot be marked resolved in this release. |
| [v3.3](https://github.com/huwanduf/P7000-SCN-Firmware/releases/tag/v3.3) · WB ±6 and landscape auto flash | Expanded both WB axes to ±6 with migration; added Auto/Off flash choices in Landscape; reduced duplicate WB callback calculations. | Landscape still defaults to flash off and follows scene initialization on re-entry. Menu/live-view blackouts were not demonstrated to be eliminated. | The user reported that everything apart from lag was working very well; no independent per-feature shooting report. |
| [v3.2.2](https://github.com/huwanduf/P7000-SCN-Firmware/releases/tag/v3.2.2) · Restore native scene Picture Control | Disabled SCN Picture Control, restored scene-generated sharpening/saturation/contrast, and removed the dedicated adjustment page. | Retained WB/ISO and metering/distortion/Active D-Lighting. Minimum shutter follows the scene, additional continuous modes remain deferred, and lag remains. | The user described it as fully usable, then requested performance research. This is user feedback, not independent testing of every scene. |
| v3.2.1 · Picture Control entry revision | Returned to the factory entry command, opened the three adjustments through the native subwindow loader, and revised exit handling. | No hardware confirmation that this revision fixed the issue. The user then chose to disable SCN Picture Control; v3.2.2 withdrew this path. | Offline checks passed; no hardware-pass record for this release. |
| v3.2 · Expanded scene controls | Opened metering, distortion control and Active D-Lighting; added a ±2 sharpening/saturation/contrast page and unified the WB background flow. | Disabled minimum shutter and restored scene exposure decisions. Additional continuous modes were deferred by user choice. The user reported a black screen in Picture Control; the other three controls opened but remained slow. | Menu feedback exists. Picture Control did not succeed, and overall acceleration was not demonstrated. |
| v3.1 · WB navigation and My Menu | Entered WB fine adjustment directly in SCN, selectively opened My Menu, and attempted a hard minimum-shutter limit. | The user reported that the shutter limit did not control exposure effectively. WB entry/exit still produced roughly one-second blackouts. The shutter changes were removed in v3.2. | Actual-operation feedback exists, but it does not establish that all features passed. |
| v3 · Shared WB/ISO and persistence | Shared two-axis ±2 offsets on top of each scene's original WB, legal ISO choices, and independent save/restore. | No dual-policy menu, fixed WB presets/color temperatures or My Menu expansion. The user found continuous scrolling through disabled WB presets. | The user explicitly confirmed basic operation and power-cycle memory. |
| [v2](https://github.com/huwanduf/P7000-SCN-Firmware/releases/tag/v2) · All-SCN NRW+JPEG | Extended support to 18 scene-menu entries: 17 manually selected scenes and Scene auto selector. | Retained native JPEG-size and special continuous-capture compatibility restrictions; not every special combination supports RAW. | The user subsequently reported success. This is not a per-item test of all 18 scenes and special combinations. |
| [v1](https://github.com/huwanduf/P7000-SCN-Firmware/releases/tag/v1) · Four-scene NRW+JPEG | Opened NRW+Fine/Normal/Basic JPEG in Portrait, Landscape, Close-up and Food. | RAW-only, Scene auto selector and the remaining scenes retained their original restrictions. | The user explicitly confirmed successful updating and shooting in all four scenes. Sample files were not independently inspected. |

## Current project direction

Open RAW+JPEG, WB/ISO and confirmed compatible controls while retaining the original SCN processing character. Given this older platform's resources and stable-operation requirements, do not import unverified P7100 code or alter clocks, hardware initialization or calibration areas. Picture Control, minimum shutter and additional continuous modes follow the current policy of retaining scene programs; the historical failures and incomplete verification remain recorded above. Not every unfinished feature can be attributed to chip performance, and earlier blackouts are not described as resolved.

## Firmware SHA-256

| Version | SHA-256 |
|---|---|
| v3.4.3 | `b147246ded1d43ff365a9e31f37565ff43676e4dc23e229946edb73e091040de` |
| v3.4.2 | `89fef5c84dba57897be26cb938c50693482997b1fcdef396ebb0f26301586900` |
| v3.4.1 | `a490e4eb36724a05e17a4db858c52902bdb1d0ee922da02a090853831894b5bd` |
| v3.4 | `c3fa493dab052dd82057b64ec86a2390cafb5d5ba14dedbe83dc964e7e110c18` |
| v3.3 | `db946841a6ded0be1ffce830bc2fb88868cd109c58931f7c5af971252ea0a4b2` |
| v3.2.2 | `f69fb7f30de084eee24d4c6a98ae51727192f98af1cad286bba81e26f942cdd6` |
| v3.2.1 | `8802ee356a5076c397b525ac7d73aab3cab9d9bfe0266453b3aaed15dad2deb8` |
| v3.2 | `c20ea390343a49b41c9cce76132fed56e3a606978f8be887af386ed4009f1587` |
| v3.1 | `d41fd80efe673917c05f9e6410ab2dfe1e15814571d050e448f4db225003c1bd` |
| v3 | `b74f89f9536c73077bc52865e4a6587b9bf75acfd505c34e6e864ff6f146a2bd` |
| v2 | `1e34e288900e954c20cca7821475f1accb0118ff91047894d3820ca8c055933d` |
| v1 | `db51086dd9d823e6819307aecda22873e4c9b73cc03bb33345b5d91c287facd7` |
