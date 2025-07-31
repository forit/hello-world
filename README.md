# Xshell Session Address Exporter / Xshell会话地址导出工具

[English](#english) | [中文](#中文)

---

## English

### Overview
This tool helps you export all connection addresses and session information from Xshell terminal emulator. It automatically searches for Xshell session files (.xsh) and extracts host addresses, ports, protocols, and other connection details.

### Features
- 🔍 **Automatic Discovery**: Finds Xshell session files in standard locations
- 📁 **Multiple Formats**: Export to CSV, JSON, or TXT formats
- 🌐 **Multi-Version Support**: Works with Xshell 6, 7, and 8
- 📊 **Detailed Information**: Extracts host, port, protocol, username, and descriptions
- 🔧 **Flexible Options**: Custom search paths and output formats

### Requirements
- Python 3.6 or higher
- Windows operating system
- Xshell installed with existing session files

### Files Included
- `xshell_export_addresses.py` - Main Python script
- `export_xshell_sessions.bat` - Windows batch file for easy execution
- `Export-XshellSessions.ps1` - PowerShell script with advanced options
- `README.md` - This documentation file

### Quick Start

#### Method 1: Using Batch File (Easiest)
1. Double-click `export_xshell_sessions.bat`
2. The script will automatically find and export all Xshell sessions
3. Check the generated files in the same directory

#### Method 2: Using PowerShell Script
1. Open PowerShell as Administrator
2. Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
3. Navigate to the script directory
4. Run: `.\Export-XshellSessions.ps1`

#### Method 3: Using Python Script Directly
```bash
# Basic usage
python xshell_export_addresses.py

# Custom path
python xshell_export_addresses.py --path "C:\Custom\Path\To\Sessions"

# Specific format
python xshell_export_addresses.py --format csv

# Custom output name
python xshell_export_addresses.py --output my_sessions
```

### Command Line Options

```
python xshell_export_addresses.py [OPTIONS]

Options:
  -p, --path PATH     Custom path to search for session files
  -f, --format FORMAT Output format: csv, json, txt, or all (default: all)
  -o, --output NAME   Output filename prefix (without extension)
  -q, --quiet         Only show summary, no detailed output
  -h, --help          Show help message
```

### Output Files

The tool generates files with timestamps to avoid overwriting:

1. **CSV Format** (`xshell_sessions_YYYYMMDD_HHMMSS.csv`)
   - Spreadsheet-compatible format
   - Easy to import into Excel or other tools

2. **JSON Format** (`xshell_sessions_YYYYMMDD_HHMMSS.json`)
   - Structured data format
   - Suitable for programming and automation

3. **TXT Format** (`xshell_addresses_YYYYMMDD_HHMMSS.txt`)
   - Human-readable text format
   - Easy to view and print

### Common Xshell Session Locations

The script automatically searches these locations:

- `%APPDATA%\NetSarang\Xshell\Sessions\`
- `%APPDATA%\Netsarang Computer\7\Xshell\Sessions\`
- `%APPDATA%\Netsarang Computer\8\Xshell\Sessions\`
- `%APPDATA%\Netsarang Computer\6\Xshell\Sessions\`
- `%USERPROFILE%\Documents\NetSarang\Xshell\Sessions\`

### Troubleshooting

**Problem**: "No session files found"
- **Solution**: Check if Xshell is installed and has been used to create sessions
- **Solution**: Manually specify the path using `--path` option

**Problem**: "Python not found"
- **Solution**: Install Python from https://python.org
- **Solution**: Make sure Python is added to PATH during installation

**Problem**: "Permission denied"
- **Solution**: Run as Administrator
- **Solution**: Check if antivirus is blocking the script

---

## 中文

### 概述
这个工具可以帮助您导出Xshell终端模拟器中的所有连接地址和会话信息。它会自动搜索Xshell会话文件(.xsh)并提取主机地址、端口、协议和其他连接详细信息。

### 功能特性
- 🔍 **自动发现**: 在标准位置查找Xshell会话文件
- 📁 **多种格式**: 导出为CSV、JSON或TXT格式
- 🌐 **多版本支持**: 适用于Xshell 6、7和8
- 📊 **详细信息**: 提取主机、端口、协议、用户名和描述
- 🔧 **灵活选项**: 自定义搜索路径和输出格式

### 系统要求
- Python 3.6或更高版本
- Windows操作系统
- 已安装Xshell且存在会话文件

### 包含文件
- `xshell_export_addresses.py` - 主Python脚本
- `export_xshell_sessions.bat` - Windows批处理文件，便于执行
- `Export-XshellSessions.ps1` - PowerShell脚本，具有高级选项
- `README.md` - 本说明文档

### 快速开始

#### 方法1：使用批处理文件（最简单）
1. 双击 `export_xshell_sessions.bat`
2. 脚本会自动查找并导出所有Xshell会话
3. 在同一目录中查看生成的文件

#### 方法2：使用PowerShell脚本
1. 以管理员身份打开PowerShell
2. 运行：`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
3. 导航到脚本目录
4. 运行：`.\Export-XshellSessions.ps1`

#### 方法3：直接使用Python脚本
```bash
# 基本用法
python xshell_export_addresses.py

# 自定义路径
python xshell_export_addresses.py --path "C:\Custom\Path\To\Sessions"

# 指定格式
python xshell_export_addresses.py --format csv

# 自定义输出名称
python xshell_export_addresses.py --output my_sessions
```

### 命令行选项

```
python xshell_export_addresses.py [选项]

选项:
  -p, --path PATH     搜索会话文件的自定义路径
  -f, --format FORMAT 输出格式：csv, json, txt, 或 all (默认: all)
  -o, --output NAME   输出文件名前缀（不含扩展名）
  -q, --quiet         仅显示摘要，不显示详细输出
  -h, --help          显示帮助信息
```

### 输出文件

工具生成带时间戳的文件以避免覆盖：

1. **CSV格式** (`xshell_sessions_YYYYMMDD_HHMMSS.csv`)
   - 电子表格兼容格式
   - 易于导入Excel或其他工具

2. **JSON格式** (`xshell_sessions_YYYYMMDD_HHMMSS.json`)
   - 结构化数据格式
   - 适用于编程和自动化

3. **TXT格式** (`xshell_addresses_YYYYMMDD_HHMMSS.txt`)
   - 人类可读的文本格式
   - 易于查看和打印

### 常见Xshell会话位置

脚本会自动搜索这些位置：

- `%APPDATA%\NetSarang\Xshell\Sessions\`
- `%APPDATA%\Netsarang Computer\7\Xshell\Sessions\`
- `%APPDATA%\Netsarang Computer\8\Xshell\Sessions\`
- `%APPDATA%\Netsarang Computer\6\Xshell\Sessions\`
- `%USERPROFILE%\Documents\NetSarang\Xshell\Sessions\`

### 故障排除

**问题**："未找到会话文件"
- **解决方案**：检查Xshell是否已安装并已用于创建会话
- **解决方案**：使用`--path`选项手动指定路径

**问题**："未找到Python"
- **解决方案**：从 https://python.org 安装Python
- **解决方案**：确保在安装时将Python添加到PATH

**问题**："权限被拒绝"
- **解决方案**：以管理员身份运行
- **解决方案**：检查杀毒软件是否阻止了脚本

### 示例输出

```
Xshell Sessions Address Exporter
========================================
Searching in: C:\Users\User\AppData\Roaming\NetSarang\Xshell\Sessions
Found 15 session files

Found 12 sessions with host information:
============================================================
  1. Production Server
     Host: 192.168.1.100
     Port: 22
     Protocol: SSH
     Username: admin

  2. Development Server
     Host: dev.example.com
     Port: 2222
     Protocol: SSH
     Username: developer

Sessions exported to: xshell_sessions_20241208_143052.csv
Sessions exported to: xshell_sessions_20241208_143052.json
Sessions exported to: xshell_addresses_20241208_143052.txt

Export completed! Found 12 sessions.
```

### 许可证
本工具仅供学习和个人使用。请确保您有权访问和导出Xshell会话文件。

### 支持
如果遇到问题，请检查：
1. Python是否正确安装
2. Xshell会话文件是否存在
3. 是否有足够的文件访问权限

---

**注意**: 本工具不会修改您的Xshell会话文件，仅读取和导出信息。