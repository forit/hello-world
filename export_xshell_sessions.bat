@echo off
chcp 65001 >nul
echo ========================================
echo Xshell 会话地址导出工具
echo Xshell Session Address Exporter
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误：未找到 Python。请先安装 Python。
    echo Error: Python not found. Please install Python first.
    pause
    exit /b 1
)

REM Check if the Python script exists
if not exist "xshell_export_addresses.py" (
    echo 错误：未找到 xshell_export_addresses.py 文件
    echo Error: xshell_export_addresses.py file not found
    pause
    exit /b 1
)

echo 正在搜索并导出 Xshell 会话...
echo Searching and exporting Xshell sessions...
echo.

REM Run the Python script
python xshell_export_addresses.py

echo.
echo 导出完成！请查看生成的文件。
echo Export completed! Please check the generated files.
echo.

REM List generated files
echo 生成的文件 / Generated files:
for %%f in (xshell_*.csv xshell_*.json xshell_*.txt) do (
    if exist "%%f" echo - %%f
)

echo.
pause