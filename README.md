# README

# RynnBot 项目资源文档

## 📁 Assets 目录说明

本目录包含 RynnBot 机器人项目的完整物料清单、3D打印模型（STL/OBJ格式）、整合包及转换工具等资源文件。

---

## 📋 文件列表

### BOM（物料清单）

*   BOM.png - 完整的物料清单表格，包含所有部件的名称、数量、单价和建议采购渠道
    

### 社区与联系方式

*   DingTalk Community.png - 钉钉开发者交流群二维码
    
*   WeChat Community.png - 微信开发者交流群二维码
    
*   WeChat Official Accounts.png - 微信公众号二维码
    
*   WeChat DAMO Assistant.png - 微信小助手二维码
    

### 3D打印模型文件（单个部件）

> _注：当前文件夹内可能混合了 LeRobot100 和 LeRobot101 的相关资源_

*   lerobot\_tablecloth.pdf - LeRobot桌布设计图（可用于A1纸1:1打印）
    
*   print\_calib\_block.stl - 机械臂校准块3D模型 (STL)
    
*   so100\_calib\_block.stl - SO-100专用校准块3D模型 (STL)
    
*   third\_cam\_mount.stl - 第三视角相机安装支架3D模型 (STL)
    
*   wrist\_cam\_mount.stl - 腕部相机安装支架3D模型 (STL)
    
*   print\_third\_cam\_mount.obj - 第三视角相机支架3D模型 (OBJ)
    
*   wrist\_cam\_mount.obj - 腕部相机支架3D模型 (OBJ)
    

### 整机/底盘整合包（ZIP压缩包）

*   lekiwi\_STL.zip - LeKiwi 可移动机械臂 STL 模型整合包
    
*   lerobot\_so101\_STL.zip - LeRobot SO-101 机械臂 STL 模型整合包
    

### 开发工具脚本

*   stl\_to\_obj.py - Python 脚本，用于将 STL 格式的 3D 模型转换为 OBJ 格式
    

---

## 🔧 主要部件清单

### 核心组件

| **部件名称** | **数量** | **预估成本** | **采购渠道** |
| --- | --- | --- | --- |
| Standard Open SO-100 & SO-101 Arms | 1 | ~1345元 | 网购 |
| 腕部USB相机 | 1 | ~203元 | 网购 |
| 第三视角USB相机 | 1 | ~193元 | 网购 |
| USB hub | 1 | ~147元 | 网购 |

### DIY部件

| **部件名称** | **数量** | **制作方式** |
| --- | --- | --- |
| 桌布 | 1 | 打印店1:1打印lerobot\_tablecloth.pdf |
| 第三视角相机支架 | 1 | 3D打印 print\_third\_cam\_mount.stl/.obj |
| 腕部相机支架 | 1 | 3D打印 wrist\_cam\_mount.stl/.obj |
| 机械臂校准块 | 1 | 3D打印 print\_calib\_block.stl |

### 紧固件

| **部件名称** | **数量** | **预估成本** | **备注** |
| --- | --- | --- | --- |
| M2x16螺丝 | 2 | ~3.5元 | 5pcs价格 |
| M2x6自攻螺丝 | 8 | ~3.5元 | 500pcs价格 |

---

## 🛠️ 工具清单

| **工具名称** | **数量** | **预估成本** | **采购渠道** |
| --- | --- | --- | --- |
| 乐泰401快干胶 | 1 | ~21元 | 网购 |
| 乐泰770促进剂 | 1 | ~84元 | 网购 |
| 魔术贴 | 1 | ~14元 | 网购 |
| 3M双面胶 | 1 | ~11元 | 网购 |

---

## 💻 格式转换工具使用指南

为了方便在 Blender 等支持 OBJ 的软件中进行渲染或二次编辑，我们提供了 [stl\_to\_obj.py](https://github.com/alibaba-damo-academy/RynnBot/blob/main/assets/stl_to_obj.py) 脚本。

使用方法：

```bash
bashpython stl_to_obj.py <输入文件名>.stl -o <输出文件名>.obj
```

示例：

```bash
bashpython stl_to_obj.py Front视角相机支架v0.3.stl -o Front视角相机支架v0.3.obj
```
---

## 📝 使用说明

1.  查看完整BOM: 打开 [BOM.png](https://github.com/alibaba-damo-academy/RynnBot/blob/main/assets/BOM.png) 查看所有部件的详细规格和采购建议
    
2.  3D打印:
    
    *   下载对应的 `.stl` 文件进行直接切片打印。
        
    *   如需修改模型或使用特定软件，可使用 `.obj` 文件或运行转换脚本。
        
3.  整机装配:
    
    *   解压 `lekiwi_STL.zip` 获取移动底盘模型。
        
    *   解压 `lerobot_so101_STL.zip` 获取机械臂主体模型。
        
4.  桌布制作: 将 `lerobot_tablecloth.pdf` 发送到打印店使用A1纸进行1:1打印
    
5.  社区交流: 扫描相关二维码加入技术社区获取支持
    

---

## 💡 注意事项

*   所有价格为参考值，实际购买时请以商家报价为准
    
*   ZIP 整合包中的模型较多，请根据具体需求选择对应版本的模型文件
    
*   组装前请仔细阅读官方装配指南