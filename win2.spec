# -*- mode: python -*-

block_cipher = None


a = Analysis(['win2.py'],
             pathex=['C:\\Users\\reall\\Anaconda3\\Lib\\site-packages\\PyQt5\\Qt\\plugins\\platforms', 'C:\\Users\\reall\\pyworks'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='win2',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
