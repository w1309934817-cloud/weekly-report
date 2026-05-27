# -*- mode: python ; coding: utf-8 -*-
import sys

_name = '周报生成器'

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('html/index.html', 'html'),
    ],
    hiddenimports=[
        'flask',
        'werkzeug',
        'waitress',
        'webview',
        'bottle',
        'proxy_tools',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'setuptools',
        'pip',
        'pkg_resources',
    ],
    noarchive=False,
    optimize=2,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=True,
    upx=False,
    upx_exclude=[],
    name=_name,
)

if sys.platform == 'darwin':
    app = BUNDLE(
        coll,
        name=_name,
        icon=None,
        bundle_identifier='com.weekly.report',
        info_plist={
            'NSHighResolutionCapable': True,
            'CFBundleShortVersionString': '1.0.0',
            'CFBundleVersion': '1.0.0',
        },
    )
