# Validation scope

English | [简体中文](validation.zh-CN.md)

## Offline checks passed for v3.4.3

- 371 Photo info menu cases: independent row switches, directional/rotary navigation, confirmation and cancellation, and the original six cells.
- 218 OSD cases: factory and invalid battery values, five bars/red one-bar low state, switches for both information views, display suspension/recovery and cache-read rate limiting.
- 20,544 native parameter/migration cases: ARM/Thumb callbacks, the read-only battery field, invalid input, P7C4 encoding/decoding, legacy-record migration and the outer restore gate.
- Firmware length, four section checksums, original bytes and change boundaries, resource rebuilding, incoming references, unchanged-region checks and bounded instruction replay of the actual resource-loading path.
- Source builds and independent patch reconstruction produce byte-identical firmware.

The bounded instruction interpreters use explicitly identified test substitutes. They are not execution on the physical ARM CPU, display hardware or Flash. The public research package retains the actual reports, original source hashes and reproduction instructions.

## Still requires hardware testing for this release

Actual battery-column typography, layout and overlap; physical keys and display-switch events; new-switch persistence after normal shutdown; sleep, video and capture-busy states; real battery-discharge behavior and MCU update intervals. Offline evidence that the factory cache can change does not establish how much capacity a particular battery currently has.

## Existing user feedback

The initial four-scene release received shooting feedback for all four scenes. Basic WB/ISO operation and power-cycle memory in V3, usability in V3.2.2, and the main V3.3 features apart from lag were confirmed by the user. This is user feedback, not an independent experiment covering every combination, and it does not establish acceptance of V3.4.3.

## Public-package preparation

The GitHub package removes personal-photo filenames/hash provenance, unnecessary local-path records and duplicate staging directories. Firmware, current source files and hash bindings remain unchanged. The public file manifest is regenerated, and source/patch reconstruction is rerun. The repository contains the current firmware and documentation; the complete historical dependencies are in the research asset.
