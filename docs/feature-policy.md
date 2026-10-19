# Feature choices and SCN character

English | [简体中文](feature-policy.zh-CN.md)

The project preserves each scene's original combination of color, exposure and capture processing, then opens compatible controls within that pipeline. On this older platform, limiting changes, reusing native parameter interfaces and avoiding additional blocking work in the display thread are the current stability strategy. This does not mean that every delay has been measured and attributed to insufficient chip performance.

| Feature | Current policy and evidence |
|---|---|
| WB | Keep each scene's original white balance and add a shared two-axis ±6 offset. The full preset/color-temperature list remains unavailable to preserve the scene's color foundation. |
| Picture Control | Use scene-generated sharpening, saturation and contrast; the SCN entry remains disabled. The earlier custom entry received black-screen reports and was withdrawn. |
| Minimum shutter speed | The SCN row is disabled, and the scene program determines exposure duration. The earlier forced-limit attempt did not work as intended and was removed in V3.2. Ordinary modes retain their original behavior. |
| Continuous shooting | Keep the original scene policy. Additional continuous-mode submissions also affect image quality, size and ISO; restoration is not sufficiently verified, so cross-scene expansion is deferred. |
| Noise reduction / custom Picture Control | Preserve scene processing and factory restrictions, without rewriting ordinary-mode or user Picture Control settings. |
| My Menu | Preserve the user's six slots, checking the actual target and scene conditions individually rather than forcing every slot to be available. |
| P7100 reference | Use it only as a comparison research lead. Its layout and platform differ; unverified code from another model is not included. |
| Performance | Do not change chip clocks, hardware initialization or calibration. Menu and live-view-return delays are still reported; no overall speed-up has been demonstrated. |
| Battery | Reuse the factory seven-level cache and group it into five bars. Do not invent voltage, 1% capacity measurements or battery-health estimates, and do not add synchronous MCU waits to the UI. |

“Preserving character” describes the feature direction, “not implemented” describes unfinished work, and “not verified” describes the evidence boundary. Historical defects are not relabeled as successfully implemented designs.
