#!/usr/bin/env python3
import os
import subprocess
import sys
from datetime import datetime

# 配置参数
TARGET_DIR = "/home/neo/下载/download/"  # 要处理的目录
PASSWORD_LIST = ["上村花论坛看小姐姐",
                 "jpdrs.cn",
                 "cosergirl.com",
                 "上老王论坛当老王",
                 "22233",
                 "蒂蒂.didi",
                 None]  # 密码数组，包含你的密码和无密码尝试
OUTPUT_ROOT = "/home/neo/下载/download/"  # 解压根目录
SUPPORTED_FORMATS = {
    '.001': '7z',
    '.mtg': '7z',
    '.cc': '7z',
    '.didi': '7z',
    '.mtuge': '7z',
    '.7z': '7z',
    '.tar': '7z',
    '.zip': '7z'  # 关键修改：zip格式使用unzip工具
}
DEBUG_MODE = True
TIMEOUT = 300  # 超时时间(秒)


def print_debug(message):
    """调试信息输出"""
    if DEBUG_MODE:
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}][调试] {message}")


def get_archive_files(target_dir):
    """获取当前目录下的压缩包"""
    archive_files = []
    if not os.path.isdir(target_dir):
        print(f"错误: 目标目录不存在 - {target_dir}")
        return archive_files

    print_debug(f"开始扫描目录: {target_dir}（非递归）")

    for file in os.listdir(target_dir):
        file_path = os.path.join(target_dir, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            if ext in SUPPORTED_FORMATS:
                full_path = os.path.abspath(file_path)
                archive_files.append((full_path, ext))
                print_debug(f"发现压缩包: {full_path} (格式: {ext})")

    print(f"共发现 {len(archive_files)} 个压缩包")
    return archive_files


def try_extract_with_password(archive_path, ext, password, output_dir):
    """尝试使用指定密码解压，支持ZIP格式自动回退到7z处理"""
    tool = SUPPORTED_FORMATS[ext]
    # 对于ZIP文件，先尝试unzip，失败则用7z重试
    tools_to_try = [tool] if ext != '.zip' else [tool, '7z']

    for current_tool in tools_to_try:
        try:
            if current_tool == '7z':
                cmd = [current_tool, 'x', f'-o{output_dir.rstrip("/\\")}', archive_path, '-y']
                if password is not None:
                    cmd.insert(2, f'-p{password}')

            elif current_tool == 'unzip':
                cmd = [current_tool, '-o']
                if password is not None:
                    cmd.extend([f'-P{password}'])
                cmd.extend([archive_path, '-d', output_dir])

            else:
                return False, "不支持的工具"

            print_debug(f"尝试解压命令: {' '.join(cmd)} (工具: {current_tool})")

            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=TIMEOUT
            )

            if result.returncode == 0:
                return True, f"成功（使用工具: {current_tool}）"
            else:
                output = ""
                try:
                    output = result.stdout.decode(sys.getfilesystemencoding(), errors='replace')
                except:
                    output = result.stdout.decode('utf-8', errors='replace')

                # 判断是否需要重试（仅ZIP文件且当前是unzip失败时）
                if ext == '.zip' and current_tool == 'unzip':
                    # 检测是否是格式不支持的错误
                    if "PK compat. v5.1" in output or "need PK compat" in output:
                        print_debug(f"unzip不支持该ZIP格式，尝试用7z重试...")
                        continue  # 继续尝试下一个工具（7z）

                # 密码错误单独处理
                if "password" in output.lower() or "密码" in output:
                    return False, "密码错误"
                return False, f"解压失败 (返回码: {result.returncode}, 工具: {current_tool})\n{output[:500]}"

        except subprocess.TimeoutExpired:
            return False, f"超时（超过{TIMEOUT}秒，工具: {current_tool}）"
        except Exception as e:
            return False, f"执行错误（工具: {current_tool}）: {str(e)}"

    # 所有工具都尝试过且失败
    return False, f"所有支持的工具都无法解压该文件"


def extract_single_archive(archive_path, ext, output_dir):
    """尝试所有密码解压单个压缩包"""
    file_name = os.path.basename(archive_path)
    print(f"\n📦 处理文件: {file_name}")

    if not os.access(archive_path, os.R_OK):
        print(f"❌ 无读取权限，跳过")
        return False
    if not os.access(output_dir, os.W_OK):
        print(f"❌ 无写入权限，跳过")
        return False

    # 尝试密码列表
    for attempt, password in enumerate(PASSWORD_LIST, 1):
        pwd_display = "无密码" if password is None else f"密码{attempt}"
        print(f"🔑 尝试 {attempt}/{len(PASSWORD_LIST)}: {pwd_display}")

        success, msg = try_extract_with_password(
            archive_path, ext, password, output_dir
        )

        if success:
            print(f"✅ 解压成功，使用{pwd_display}，保存至: {output_dir}")
            return True
        else:
            print(f"❌ 尝试失败: {msg}")
            if "密码" not in msg:
                break

    print(f"❌ 所有密码尝试均失败，无法解压 {file_name}")
    return False


def check_dependencies():
    """检查所需解压工具"""
    print_debug("检查依赖工具...")
    missing = []
    for tool in set(SUPPORTED_FORMATS.values()):
        try:
            subprocess.run(
                [tool, '--version'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            missing.append(tool)

    if missing:
        print(f"错误: 缺少必要工具，请安装: {', '.join(missing)}")
        print("安装参考: sudo apt install p7zip-full unzip")
        return False
    return True


def main():
    print("===== 多密码压缩包解压工具 =====")
    print(f"目标目录: {TARGET_DIR}")
    print(f"解压目录: {OUTPUT_ROOT}")
    print(f"支持格式: {', '.join(SUPPORTED_FORMATS.keys())}")
    print(f"密码尝试列表: {['无密码' if p is None else '***' for p in PASSWORD_LIST]}")

    if not check_dependencies():
        sys.exit(1)

    archives = get_archive_files(TARGET_DIR)
    if not archives:
        print("未发现可处理的压缩包，退出")
        return

    success_count = 0
    fail_count = 0

    for idx, (path, ext) in enumerate(archives, 1):
        print(f"\n----- 第 {idx}/{len(archives)} 个文件 -----")
        if extract_single_archive(path, ext, OUTPUT_ROOT):
            success_count += 1
        else:
            fail_count += 1

    print("\n===== 处理完成 =====")
    print(f"总文件数: {len(archives)}")
    print(f"成功: {success_count} 个")
    print(f"失败: {fail_count} 个")


if __name__ == "__main__":
    main()