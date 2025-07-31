# Xshell Session Address Exporter
# PowerShell版本的Xshell会话地址导出工具

[CmdletBinding()]
param(
    [Parameter(HelpMessage="自定义搜索路径 / Custom search path")]
    [string]$Path,
    
    [Parameter(HelpMessage="输出格式 / Output format")]
    [ValidateSet("csv", "json", "txt", "all")]
    [string]$Format = "all",
    
    [Parameter(HelpMessage="输出文件名前缀 / Output filename prefix")]
    [string]$OutputPrefix = "xshell_sessions",
    
    [Parameter(HelpMessage="静默模式 / Quiet mode")]
    [switch]$Quiet
)

# 设置控制台编码为UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "========================================" -ForegroundColor Green
Write-Host "Xshell 会话地址导出工具" -ForegroundColor Green
Write-Host "Xshell Session Address Exporter" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# 检查Python是否可用
try {
    $pythonVersion = python --version 2>$null
    if (-not $pythonVersion) {
        throw "Python not found"
    }
    Write-Host "Python 版本: $pythonVersion" -ForegroundColor Yellow
} catch {
    Write-Host "错误：未找到 Python。请先安装 Python。" -ForegroundColor Red
    Write-Host "Error: Python not found. Please install Python first." -ForegroundColor Red
    Read-Host "按任意键退出 / Press any key to exit"
    exit 1
}

# 检查Python脚本是否存在
$scriptPath = Join-Path $PSScriptRoot "xshell_export_addresses.py"
if (-not (Test-Path $scriptPath)) {
    Write-Host "错误：未找到 xshell_export_addresses.py 文件" -ForegroundColor Red
    Write-Host "Error: xshell_export_addresses.py file not found" -ForegroundColor Red
    Read-Host "按任意键退出 / Press any key to exit"
    exit 1
}

Write-Host "正在搜索并导出 Xshell 会话..." -ForegroundColor Yellow
Write-Host "Searching and exporting Xshell sessions..." -ForegroundColor Yellow
Write-Host ""

# 构建Python命令参数
$pythonArgs = @($scriptPath)

if ($Path) {
    $pythonArgs += "--path", $Path
}

if ($Format) {
    $pythonArgs += "--format", $Format
}

if ($OutputPrefix -and $OutputPrefix -ne "xshell_sessions") {
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $outputName = "${OutputPrefix}_${timestamp}"
    $pythonArgs += "--output", $outputName
}

if ($Quiet) {
    $pythonArgs += "--quiet"
}

# 运行Python脚本
try {
    & python @pythonArgs
    if ($LASTEXITCODE -ne 0) {
        throw "Python script failed with exit code $LASTEXITCODE"
    }
} catch {
    Write-Host "执行出错: $_" -ForegroundColor Red
    Write-Host "Error during execution: $_" -ForegroundColor Red
    Read-Host "按任意键退出 / Press any key to exit"
    exit 1
}

Write-Host ""
Write-Host "导出完成！请查看生成的文件。" -ForegroundColor Green
Write-Host "Export completed! Please check the generated files." -ForegroundColor Green
Write-Host ""

# 列出生成的文件
Write-Host "生成的文件 / Generated files:" -ForegroundColor Cyan
$generatedFiles = Get-ChildItem -Path . -Name "xshell_*.*" | Where-Object { $_ -match '\.(csv|json|txt)$' }
foreach ($file in $generatedFiles) {
    $fileInfo = Get-Item $file
    $size = [math]::Round($fileInfo.Length / 1KB, 2)
    Write-Host "  - $file ($size KB)" -ForegroundColor White
}

if (-not $generatedFiles) {
    Write-Host "  未找到生成的文件 / No generated files found" -ForegroundColor Yellow
}

Write-Host ""
Read-Host "按任意键退出 / Press any key to exit"