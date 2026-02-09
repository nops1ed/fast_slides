import os
from typing import Optional


class Config:
    """配置管理类"""
    
    def __init__(self, target_filepath: str):
        # 路径配置
        self.project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.static_path = os.path.join(self.project_root, "fast_slides", "static")
        self.backup_path = os.path.join(self.project_root, "fast_slides", "backup")
        self.template_from = os.path.join(self.backup_path, "template", "basetemp.html")
        self.authortemp_from = os.path.join(self.backup_path, "template", "authortemp.html")
        
        # 操作符配置
        self.op_first_section = "\n---\n"
        self.op_second_section = "\n----\n"
        self.op_animate_section = "\n++++\n"
        self.op_index_fragment = "\n--\n"
        self.op_front_matter = "\n+++++\n"
        
        # 文件信息
        self.filename = os.path.basename(target_filepath)
        self.filepath = os.path.abspath(target_filepath)
        self.output_foldname = "dist"
        self.output_filename = "index.html"
        self.output_foldpath = os.path.join(os.path.dirname(self.filepath), self.output_foldname)
        self.output_filepath = os.path.join(self.output_foldpath, self.output_filename)
        self.static_foldpath = os.path.join(self.output_foldpath, "static")
        self.images_foldname = "img"  # 如果要修改还要修炼static下的img文件名，template中icon的文件路径
        self.images_foldpath = os.path.join(self.static_foldpath, self.images_foldname)
        
        # 内容
        self.content: str = ""  # MD内容
        self.title: str = ""
        self.body: str = ""
        
        # 模板
        self.template: Optional[str] = None
        self.author_template: Optional[str] = None
    
    def get_title(self) -> str:
        """获取标题"""
        if not self.title and self.filename:
            return "".join(self.filename.split(".")[:-1])
        return self.title
    
    def set_content(self, content: str) -> None:
        """设置内容"""
        self.content = content
    
    def set_title(self, title: str) -> None:
        """设置标题"""
        self.title = title
    
    def set_body(self, body: str) -> None:
        """设置正文"""
        self.body = body
    
    def set_template(self, template: str) -> None:
        """设置模板"""
        self.template = template
    
    def set_author_template(self, author_template: str) -> None:
        """设置作者模板"""
        self.author_template = author_template
