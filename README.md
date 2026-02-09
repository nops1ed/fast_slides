# fast-slides

## 🌍 Language

- [English](./README.md) (default)
- [中文](./README_zh.md)

## 📣 宣传语 / Promotional

### English
Tired of creating PowerPoint presentations? Want to quickly create slides using Markdown?

fast-slides is a fast and elegant slide generator from Markdown. No complex operations needed - just write simple Markdown syntax to generate beautiful, professional slides.

## 📖 项目介绍 / Project Introduction

### English
fast-slides is a tool for generating slides from Markdown files, providing simple syntax and elegant themes to help you quickly create professional slides.

## ✨ 功能特性 / Features

### English
- **Simple Markdown syntax**：Easy-to-learn extension syntax for creating slides
- **Real-time preview**：Watch for file changes and auto-recompile
- **Elegant theme**：Based on the clean slide style of Professor Jiang Yanyan
- **Easy installation**：Support for installation from source and command-line usage
- **Feature-rich**：Support for fragments, animations, images, code highlighting, and more
- **Packaging functionality**：Easily create ZIP files of slides for convenient transfer and sharing

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

### English

#### Basic Structure
- **Horizontal slides**：Use `\n---\n` (three dashes)
- **Vertical slides**：Use `\n----\n` (four dashes)
- **Animated slides**：Use `\n++++\n` (four pluses) for fade-in effects
- **Fragments**：Use `\n--\n` (two dashes) for sequential appearance
- **Author info**：Use `\n+++++\n` (five pluses) to separate author info from content

#### Example

```markdown
# Slide Title

## Introduction

--

This is a fragment that appears after the first slide content

---

## Second Slide

Content of second slide

++++

This part will fade in

++++

This part will fade in next

----

## Vertical Slide

Content of vertical slide

+++++
{
  "author": {
    "name": "Author Name",
    "url": "https://example.com"
  },
  "departments": [
    {
      "name": "Department",
      "url": "https://example.com",
      "img": "./img/logo.jpg"
    }
  ]
}
```

## ⚠️ 注意事项 / Notes

### English
1. **Python version**：Requires Python 3.9 or higher
2. **Dependency installation**：Please ensure all necessary dependencies are installed
3. **File path**：Please ensure you run scripts in the project root directory
4. **Markdown syntax**：Please use correct Markdown syntax to create slides
5. **Image paths**：If slides contain images, ensure image paths are correct
6. **Cross-machine usage**：Packaged slides can be used on machines without fast-slides installed
7. **Browser compatibility**：Modern browsers (Chrome, Firefox, Safari) are recommended for viewing slides
8. **Network connection**：Initial build requires network connection to download necessary resources

## 🔄 跨机器使用 / Cross-machine Usage

### English
To use the slides on another machine without installing any dependencies：

1. **Pack the slides**：
   - On macOS/Linux：Run `./pack.sh`
   - On Windows：Run `pack.bat`

2. **Transfer the ZIP file**：Transfer the generated ZIP file to the target machine

3. **Extract the ZIP file**：Extract the ZIP file on the target machine

4. **Open the slides**：Open the `index.html` file in a browser to view the slides

The slides are fully self-contained and do not require any internet connection or additional software.

## 📁 项目结构 / Project Structure

### English
```
fast_slides/
  ├── converter.py      # Core conversion logic
  ├── config.py         # Configuration management
  ├── cli.py            # Command-line interface
  ├── util/             # Utility functions
  ├── static/           # Static files (CSS, JS, etc.)
  └── backup/           # Backup and template files
run.py                  # Main run script
start.sh               # macOS/Linux launch script
start.bat              # Windows launch script
pack.sh                # macOS/Linux packaging script
pack.bat               # Windows packaging script
sample_slide.md        # Sample slide file
```

## 🎉 致谢 / Acknowledgements

### English
- **Inspired by**：[Professor Jiang Yanyan](https://ics.nju.edu.cn/~jyy/) from Nanjing University
- **Based on**：[jyyslide-md](https://github.com/zweix123/jyyslide-md)

## 📄 许可证 / License

[MIT](LICENSE) © Richard Littauer