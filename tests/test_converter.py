import os
import tempfile
import pytest
from fast_slides.converter import SlideConverter
from fast_slides.config import Config


class TestConfig:
    """测试配置类"""
    
    def test_init(self):
        """测试初始化"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write('# Test Slide')
            temp_file = f.name
        
        try:
            config = Config(temp_file)
            assert config.filename == os.path.basename(temp_file)
            assert config.filepath == os.path.abspath(temp_file)
            assert config.output_foldpath == os.path.join(os.path.dirname(temp_file), 'dist')
        finally:
            os.unlink(temp_file)
    
    def test_get_title(self):
        """测试获取标题"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write('# Test Slide')
            temp_file = f.name
        
        try:
            config = Config(temp_file)
            # 临时文件的名称是随机生成的，所以我们只需要断言它不为空
            assert config.get_title() != ''
            # 测试自定义标题
            config.set_title('Custom Title')
            assert config.get_title() == 'Custom Title'
        finally:
            os.unlink(temp_file)


class TestSlideConverter:
    """测试幻灯片转换器"""
    
    def test_convert(self):
        """测试转换功能"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # 创建测试 Markdown 文件
            test_md = os.path.join(temp_dir, 'test.md')
            with open(test_md, 'w', encoding='utf-8') as f:
                f.write('# Test Slide\n\nContent\n\n---\n\n## Second Slide')
            
            # 执行转换
            converter = SlideConverter(test_md)
            converter.convert()
            
            # 检查输出文件
            output_file = os.path.join(temp_dir, 'dist', 'index.html')
            assert os.path.exists(output_file)
            
            # 检查输出内容
            with open(output_file, 'r', encoding='utf-8') as f:
                content = f.read()
                assert 'Test Slide' in content
                assert 'Second Slide' in content


if __name__ == '__main__':
    pytest.main(['-v', __file__])
