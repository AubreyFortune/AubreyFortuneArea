# AubreyFortuneArea

一个零第三方运行时依赖的 Python 命令行示例工程，要求 Python 3.10 或更高版本。

## 运行

在项目根目录执行：

```bash
python -m pip install -e .
aubrey-area Aubrey
```

输出：

```text
Hello, Aubrey! Welcome to AubreyFortuneArea.
```

不传名字时会默认问候 `world`。

## 测试

```bash
python -m unittest discover -s tests
```

## 目录结构

```text
src/aubrey_fortune_area/  # 应用代码
tests/                    # 单元测试
pyproject.toml            # 项目与命令行入口配置
```
