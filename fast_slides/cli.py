import click
import os
from fast_slides.converter import converter
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import webbrowser


class SlideEventHandler(FileSystemEventHandler):
    """幻灯片文件事件处理器"""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
    
    def on_modified(self, event):
        """文件修改事件"""
        if event.src_path == self.filepath:
            click.echo(f"File {self.filepath} modified, recompiling...")
            try:
                converter(self.filepath)
                click.echo("Compilation successful!")
            except Exception as e:
                click.echo(f"Compilation error: {e}")


@click.group()
def cli():
    """fast-slides: A fast and elegant slide generator from Markdown"""
    pass


@cli.command()
@click.argument('filepath', type=click.Path(exists=True, file_okay=True, dir_okay=False))
def build(filepath):
    """Build slides from Markdown file"""
    click.echo(f"Building slides from {filepath}...")
    try:
        converter(filepath)
        output_dir = os.path.join(os.path.dirname(filepath), "dist")
        output_file = os.path.join(output_dir, "index.html")
        click.echo(f"Build successful! Output file: {output_file}")
    except Exception as e:
        click.echo(f"Build error: {e}")


@cli.command()
def init():
    """Initialize a new slide project"""
    # 这里可以实现初始化新项目的功能
    click.echo("Initializing new slide project...")
    # 示例：创建默认的 Markdown 文件
    default_content = """# Slide Title

## Introduction

--

This is a fragment

---

## Second Slide

Content of second slide
"""
    with open("slide.md", "w", encoding="utf-8") as f:
        f.write(default_content)
    click.echo("Created default slide.md file")


@cli.command()
@click.argument('filepath', type=click.Path(exists=True, file_okay=True, dir_okay=False))
@click.option('--watch', '-w', is_flag=True, help='Watch for file changes and recompile')
@click.option('--serve', '-s', is_flag=True, help='Serve slides and open in browser')
def start(filepath, watch, serve):
    """Start slide project with optional watch and serve"""
    # 首先构建一次
    click.echo(f"Building slides from {filepath}...")
    try:
        converter(filepath)
        output_dir = os.path.join(os.path.dirname(filepath), "dist")
        output_file = os.path.join(output_dir, "index.html")
        click.echo(f"Build successful! Output file: {output_file}")
        
        # 如果需要服务和打开浏览器
        if serve:
            click.echo("Opening slides in browser...")
            import subprocess
            subprocess.run(["open", output_file])  # 使用系统默认程序打开
        
        # 如果需要监视文件变化
        if watch:
            click.echo(f"Watching {filepath} for changes...")
            event_handler = SlideEventHandler(filepath)
            observer = Observer()
            observer.schedule(event_handler, os.path.dirname(filepath), recursive=False)
            observer.start()
            
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                observer.stop()
                observer.join()
                click.echo("Watch stopped")
                
    except Exception as e:
        click.echo(f"Error: {e}")


if __name__ == "__main__":
    cli()
