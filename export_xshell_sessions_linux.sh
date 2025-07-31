#!/bin/bash

# Xshell Session Address Exporter for Linux/Unix
# Xshell会话地址导出工具 - Linux/Unix版本

echo "========================================"
echo "Xshell 会话地址导出工具"
echo "Xshell Session Address Exporter"
echo "========================================"
echo ""

# Check if Python is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    # Check if python is Python 3
    if python -c "import sys; sys.exit(0 if sys.version_info >= (3, 6) else 1)" 2>/dev/null; then
        PYTHON_CMD="python"
    else
        echo "错误：需要 Python 3.6 或更高版本"
        echo "Error: Python 3.6 or higher is required"
        exit 1
    fi
else
    echo "错误：未找到 Python。请先安装 Python。"
    echo "Error: Python not found. Please install Python first."
    exit 1
fi

echo "使用 Python 命令: $PYTHON_CMD"
echo "Using Python command: $PYTHON_CMD"

# Check if the Python script exists
if [ ! -f "xshell_export_addresses.py" ]; then
    echo "错误：未找到 xshell_export_addresses.py 文件"
    echo "Error: xshell_export_addresses.py file not found"
    exit 1
fi

echo ""
echo "正在搜索并导出 Xshell 会话..."
echo "Searching and exporting Xshell sessions..."
echo ""

# Run the Python script
$PYTHON_CMD xshell_export_addresses.py "$@"

if [ $? -eq 0 ]; then
    echo ""
    echo "导出完成！请查看生成的文件。"
    echo "Export completed! Please check the generated files."
    echo ""
    
    # List generated files
    echo "生成的文件 / Generated files:"
    for file in xshell_*.{csv,json,txt}; do
        if [ -f "$file" ]; then
            size=$(du -h "$file" | cut -f1)
            echo "  - $file ($size)"
        fi
    done
else
    echo ""
    echo "导出过程中出现错误"
    echo "Error occurred during export"
fi

echo ""
read -p "按回车键退出 / Press Enter to exit..." dummy