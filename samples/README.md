# fast-slides 样例说明

本文件夹包含 fast-slides 的示例文件，用于展示不同功能的使用方法。

## 样例文件

### 1. basic.md

**基本功能演示**

- 基本幻灯片结构
- 水平幻灯片
- 垂直幻灯片
- 基本 Markdown 语法
- 列表、代码、引用等

### 2. advanced.md

**高级功能演示**

- 渐变垂直幻灯片
- 数学公式
- 多语言代码高亮
- 图片布局
- 复杂列表

### 3. with-author.md

**带作者信息的演示**

- 作者信息设置
- 部门信息设置
- 作者图片设置

## 使用方法

### 构建样例

```bash
# 构建基本样例
fast-slides build samples/basic.md

# 构建高级样例
fast-slides build samples/advanced.md

# 构建带作者信息的样例
fast-slides build samples/with-author.md
```

### 实时预览

```bash
# 启动实时预览
fast-slides start samples/basic.md --watch --serve
```

## 输出位置

构建完成后，会在 `samples/dist` 文件夹中生成幻灯片文件 `index.html`。

## 注意事项

- 样例中使用了在线占位图片，需要网络连接才能正常显示
- 数学公式需要支持 LaTeX 的浏览器或插件
- 代码高亮依赖于 Pygments 库
