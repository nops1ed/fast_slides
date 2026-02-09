# fast-slides

## 🌍 Language

- [English](./README.md) (default)
- [中文](./README_zh.md)

## 📣 宣传语 / Promotional

### 简体中文
觉得制作 PowerPoint 感到烦躁吗？想快速通过 Markdown 来制作 slides 吗？

fast-slides 是一个快速、优雅的 Markdown 幻灯片生成工具。无需复杂的操作，只需编写简单的 Markdown 语法，即可生成美观、专业的幻灯片。

## 📖 项目介绍 / Project Introduction

### 简体中文
fast-slides 是一个从 Markdown 文件生成幻灯片的工具，它提供了简洁的语法和优雅的主题，让您可以快速创建专业的幻灯片。

## ✨ 功能特性 / Features

### 简体中文
- **简洁的 Markdown 语法**：易于学习的扩展语法，用于创建幻灯片
- **实时预览**：监视文件变化并自动重新编译
- **优雅的主题**：基于蒋炎岩教授的简洁幻灯片风格
- **方便的安装**：支持从源代码安装和命令行使用
- **丰富的功能**：支持片段、动画、图片、代码高亮等
- **打包功能**：轻松创建幻灯片的 ZIP 文件，方便传输和分享

## 🚀 安装方法 / Installation

### 从源代码安装 / From Source

```bash
git clone https://github.com/zweix123/fast-slides.git
cd fast-slides
# 安装依赖
pip3 install requests jinja2 markdown pyquery pygments lxml pyyaml click watchdog
```

## 📦 使用方法 / Usage

### 命令行接口 / Command-line Interface

```bash
# 构建幻灯片
python3 run.py build slide.md

# 初始化新项目
python3 run.py init

# 启动实时预览
python3 run.py start slide.md --watch --serve
```

### 启动脚本 / Launch Scripts

#### macOS / Linux

```bash
# 构建默认幻灯片 (sample_slide.md)
./start.sh

# 构建指定文件
./start.sh your_file.md
```

#### Windows

```batch
:: 构建默认幻灯片 (sample_slide.md)
start.bat

:: 构建指定文件
start.bat your_file.md
```

### 打包功能 / Packaging Functionality

#### macOS / Linux

```bash
# 打包幻灯片
./pack.sh
```

#### Windows

```batch
:: 打包幻灯片
pack.bat
```

## 📝 Markdown 语法 / Markdown Syntax

### 简体中文

#### 基本结构
- **水平幻灯片**：使用 `\n---\n`（三个破折号）
- **垂直幻灯片**：使用 `\n----\n`（四个破折号）
- **动画幻灯片**：使用 `\n++++\n`（四个加号）用于淡入效果
- **片段**：使用 `\n--\n`（两个破折号）用于顺序显示
- **作者信息**：使用 `\n+++++\n`（五个加号）分隔作者信息和内容

#### 示例

```markdown
# 幻灯片标题

## 介绍

--

这是一个片段，会在第一张幻灯片内容之后显示

---

## 第二张幻灯片

第二张幻灯片的内容

++++

这部分会淡入

++++

这部分会接下来淡入

----

## 垂直幻灯片

垂直幻灯片的内容

+++++
{
  "author": {
    "name": "作者名称",
    "url": "https://example.com"
  },
  "departments": [
    {
      "name": "部门",
      "url": "https://example.com",
      "img": "./img/logo.jpg"
    }
  ]
}
```

## ⚠️ 注意事项 / Notes

### 简体中文
1. **Python 版本**：需要 Python 3.9 或更高版本
2. **依赖安装**：请确保安装了所有必要的依赖包
3. **文件路径**：请确保在项目根目录中运行脚本
4. **Markdown 语法**：请使用正确的 Markdown 语法来创建幻灯片
5. **图片路径**：如果幻灯片中包含图片，请确保图片路径正确
6. **跨机器使用**：打包后的幻灯片可以在没有安装 fast-slides 的机器上使用
7. **浏览器兼容性**：建议使用现代浏览器（如 Chrome、Firefox、Safari）查看幻灯片
8. **网络连接**：首次构建时需要网络连接来下载必要的资源

## 🔄 跨机器使用 / Cross-machine Usage

### 简体中文
要在另一台机器上使用幻灯片，无需安装任何依赖：

1. **打包幻灯片**：
   - 在 macOS/Linux 上：运行 `./pack.sh`
   - 在 Windows 上：运行 `pack.bat`

2. **传输 ZIP 文件**：将生成的 ZIP 文件传输到目标机器

3. **解压 ZIP 文件**：在目标机器上解压 ZIP 文件

4. **打开幻灯片**：在浏览器中打开 `index.html` 文件查看幻灯片

幻灯片是完全自包含的，不需要任何互联网连接或额外的软件。

## 📁 项目结构 / Project Structure

### 简体中文
```
fast_slides/
  ├── converter.py      # 核心转换逻辑
  ├── config.py         # 配置管理
  ├── cli.py            # 命令行接口
  ├── util/             # 工具函数
  ├── static/           # 静态文件（CSS、JS 等）
  └── backup/           # 备份和模板文件
run.py                  # 主运行脚本
start.sh               # macOS/Linux 启动脚本
start.bat              # Windows 启动脚本
pack.sh                # macOS/Linux 打包脚本
pack.bat               # Windows 打包脚本
sample_slide.md        # 示例幻灯片文件
```

## 🎉 致谢 / Acknowledgements

### 简体中文
- **灵感来源**：南京大学 [蒋炎岩教授](https://ics.nju.edu.cn/~jyy/)
- **基于**：[jyyslide-md](https://github.com/zweix123/jyyslide-md)

## 📄 许可证 / License

[MIT](LICENSE) © Richard Littauer