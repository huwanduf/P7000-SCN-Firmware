# 安装与回退

[English](installation.md) | 简体中文

仅适用于 Nikon COOLPIX P7000。首次安装前先完成 [官方 1.2 升级](https://downloadcenter.nikonimglib.com/zh-cn/download/fw/45.html)；原厂版本已为 1.2 时无需重复官方升级。官方页面给出的 SD 根目录 firmware 文件夹方法也是本项目采用的安装结构。

## 复制到 SD 卡

下载 `P7000-v3.4.3-SD.zip`，解压后把 **firmware 文件夹整个拖到卡根目录**：

```text
SD卡根目录/
└── firmware/
    └── firmware.bin
```

README、研究资料和源码不用复制到 SD 卡。不要把固件改名，也不要多套一层 P7000-v3.4.3-SD 或项目文件夹。复制前保留原照片备份；若卡上已有 firmware 文件夹，先在电脑另存旧固件，避免混用。

## 相机更新

使用电量充足的电池，在相机关机时插卡，开机后进入 **设置 → 固件版本 → 更新**，按提示操作。升级期间不操作按键、不关闭相机或取出电池/卡。完成后按提示正常关机，取出卡再开机。

相机版本依旧显示 **1.2**，这不是更新失败。项目的 v3.4.3 等编号仅用于区分扩展版本。无需依次安装项目历史版本；在官方 1.2 基线上使用本次完整固件。

首次确认可检查：SCN 画质中的 NRW+JPEG、WB 两轴 ±6、照片信息表中水平仪左侧的电池列。新功能的最终表现仍须在自己的相机上验收。

## 回退

完整 research 包附 V3.4.2 和 V3.3 完整回退文件。分别取相应目录内的 firmware 文件夹，按同一 SD 更新流程操作，不要混合文件。

V3.4.3 使用 P7C4 标签的同一 12 字节独立记录。较早版本不识别新标签，回退后 SCN 共享调整可能恢复安全默认，需要重设；普通模式、U 档和校准区没有借用。回退文件仅适用于仍能正常进入升级菜单的相机，未验证为不开机救砖方式。

当前固件 SHA-256：`b147246ded1d43ff365a9e31f37565ff43676e4dc23e229946edb73e091040de`。macOS/Linux 可运行 `shasum -a 256 firmware/firmware.bin`；Windows PowerShell 可运行 `Get-FileHash firmware/firmware.bin -Algorithm SHA256`。
