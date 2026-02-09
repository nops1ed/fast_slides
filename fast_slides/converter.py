import os
import shutil
import json
import yaml
from jinja2 import Template
from pyquery import PyQuery  # type: ignore

from fast_slides.config import Config
from fast_slides.util import md_util
from fast_slides.util.file_util import read, write


class MarkdownProcessor:
    """Markdown 处理器"""
    
    def __init__(self, config: Config):
        self.config = config
    
    def process_front_matter(self) -> None:
        """处理前置内容"""
        if self.config.op_front_matter not in self.config.content:
            self.config.set_author_template("")
            return

        parts = self.config.content.split(self.config.op_front_matter)

        front_matter = parts[0]
        self.config.set_content("".join(parts[1:]))

        try:
            data = json.loads(front_matter)
        except Exception as e:
            try:
                data = yaml.load(front_matter, Loader=yaml.SafeLoader)
            except Exception as e:
                # 如果解析失败，不设置作者模板
                self.config.set_author_template("")
                return

        # 处理部门图片
        for department in data["departments"]:
            if "img" in department:
                # 这里会在 ImageHandler 中处理
                pass

        # 渲染作者模板
        author_template_content = read(self.config.authortemp_from)
        template = Template(author_template_content)
        self.config.set_author_template(template.render(author=data["author"], departments=data["departments"]))
    
    def process_html_elements(self, before_html: str) -> str:
        """处理 HTML 元素"""
        temp_html = "<html><body>{}</body></html>".format(before_html)
        page = PyQuery(temp_html)
        e = page
        for item in e("h1").parent():
            t = PyQuery(item)
            t.wrap("<div style='width:100%'>")
            t.wrap("<div class='center middle'>")
        class_data = {
            "ul": "list-disc font-serif",
            "li": "ml-8",
            "h2": "text-xl mt-2 pb-2 font-sans",
            "h1": "text-2xl mt-2 font-sans",
            "p": "font-serif my-1",
            "pre": "bg-gray-100 overflow-x-auto rounded p-2 mb-2 mt-2",
        }
        for k, v in class_data.items():
            for item in e(k):
                t = PyQuery(item)
                t.add_class(v)
        page = e
        items = page("body").children()
        return "".join([str(PyQuery(e)) for e in items])
    
    def process_terminal(self, semi_html: str) -> str:
        """处理终端"""
        semi_html += self.config.author_template or ""
        self.config.set_author_template("")
        temp = "<div>" + semi_html + "</div>"
        semi_html = self.process_html_elements(temp)
        return semi_html
    
    def vertical_to_fragment(self, vertical: str) -> str:
        """垂直幻灯片转片段"""
        fragments = vertical.split(self.config.op_index_fragment)

        fragment_list = [md_util.md_to_html(fragments[0])]
        template = "<div class='fragment' data-fragment-index='{}'>{}</div>"

        for i in range(1, len(fragments)):
            fragment_list.append(template.format(i, md_util.md_to_html(fragments[i])))

        return "".join(fragment_list)
    
    def vertical_to_animate(self, vertical: str) -> str:
        """垂直幻灯片转动画"""
        animates = vertical.split(self.config.op_animate_section)

        animate_list = list()
        template = "<div class='fragment fade-in'>{}</div>"

        for i in range(len(animates)):
            animate_list.append(template.format(md_util.md_to_html(animates[i])))

        return "".join(animate_list)
    
    def horizontal_to_vertical(self, horizontal: str) -> str:
        """水平幻灯片转垂直幻灯片"""
        verticals_divided_by_second = horizontal.split(self.config.op_second_section)

        sections = list()
        template_second = "<section>{}</section>"

        for vertical_divided_by_second in verticals_divided_by_second:
            if vertical_divided_by_second.isspace():
                continue
            if self.config.op_animate_section in vertical_divided_by_second:
                # 对于渐变垂直幻灯片，我们将其作为单个 section 处理，内部使用 fragment
                template_animate = "<section data-auto-animate>{}</section>"
                sections.append(
                    template_animate.format(
                        self.process_terminal(
                            self.vertical_to_animate(vertical_divided_by_second)
                        )
                    )
                )
            elif self.config.op_index_fragment in vertical_divided_by_second:
                sections.append(
                    template_second.format(
                        self.process_terminal(self.vertical_to_fragment(vertical_divided_by_second))
                    )
                )
            else:
                sections.append(
                    template_second.format(
                        self.process_terminal(md_util.md_to_html(vertical_divided_by_second))
                    )
                )

        return "".join(sections)
    
    def md_divide_to_horizontal(self, content: str) -> str:
        """Markdown 分割为水平幻灯片"""
        horizontals = content.split(self.config.op_first_section)

        sections = list()
        template = "<section>{}</section>"

        for horizontal in horizontals:
            if horizontal.isspace():
                continue
            html_second_sections = self.horizontal_to_vertical(horizontal)

            html = template.format(html_second_sections)
            sections.append(html)

        return "".join(sections)
    
    def get_body(self, content: str) -> str:
        """获取正文"""
        return self.md_divide_to_horizontal(content)


class ImageHandler:
    """图片处理器"""
    
    def __init__(self, config: Config):
        self.config = config
    
    def process_images(self) -> None:
        """处理图片"""
        def func(link):
            from fast_slides.util.file_util import get_image_to_target
            new_name, err = get_image_to_target(
                link, self.config.filepath, self.config.images_foldpath
            )

            return (
                os.path.join(".", "static", self.config.images_foldname, new_name)
                if err is False
                else ""
            ), err

        self.config.set_content(md_util.process_images(self.config.content, func))


class TemplateRenderer:
    """模板渲染器"""
    
    def __init__(self, config: Config):
        self.config = config
    
    def render(self) -> None:
        """渲染模板"""
        template_content = read(self.config.template_from)
        template = Template(template_content)
        rendered_template = template.render(
            title=self.config.get_title(),
            body=self.config.body
        )
        self.config.set_template(rendered_template)


class SlideConverter:
    """Slide converter"""
    
    def __init__(self, target_filepath: str):
        try:
            self.config = Config(target_filepath)
            self.markdown_processor = MarkdownProcessor(self.config)
            self.image_handler = ImageHandler(self.config)
            self.template_renderer = TemplateRenderer(self.config)
        except Exception as e:
            raise Exception(f"[CONVERTER] Init failed: {str(e)}")
    
    def process_static(self) -> None:
        """Process static files"""
        try:
            if os.path.exists(self.config.output_foldpath):
                shutil.rmtree(self.config.output_foldpath)
            os.makedirs(self.config.output_foldpath)
            shutil.copytree(self.config.static_path, self.config.static_foldpath)
        except Exception as e:
            raise Exception(f"[CONVERTER] Static files processing failed: {str(e)}")
    
    def convert(self) -> None:
        """Execute conversion process"""
        try:
            # Process static files
            self.process_static()
            
            # Read Markdown content
            content = read(self.config.filepath)
            self.config.set_content(content)
            
            # Process front matter
            self.markdown_processor.process_front_matter()
            
            # Process images
            self.image_handler.process_images()
            
            # Convert Markdown to HTML
            body = self.markdown_processor.get_body(self.config.content)
            self.config.set_body(body)
            
            # Render template
            self.template_renderer.render()
            
            # Write output file
            if self.config.template:
                write(self.config.output_filepath, self.config.template)
        except Exception as e:
            raise Exception(f"[CONVERTER] Conversion failed: {str(e)}")


def converter(filepath: str) -> None:
    """Main conversion function"""
    try:
        converter = SlideConverter(filepath)
        converter.convert()
    except Exception as e:
        raise Exception(f"[CONVERTER] Failed: {str(e)}")
