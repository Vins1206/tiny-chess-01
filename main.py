# tiny-chess-01 loader: the engine is stored in payload.bin
import lzma,os
_dir=os.path.dirname(os.path.abspath(__file__))
_b=open(os.path.join(_dir,"payload.bin"),"rb").read()
exec( lzma.decompress(_b, format=lzma.FORMAT_XZ) )
