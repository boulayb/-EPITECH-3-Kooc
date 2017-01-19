from cnorm import nodes
from kooc import Kooc
import os.path


class KoocImport(nodes.Raw):
    def __init__(self, filename, srcpath, koocdata):
        super(KoocImport, self).__init__("#include \"" + filename[:-2] + filename[-1] + "\"\n")
        if os.path.isfile(srcpath + "/" + filename) is not True:
            raise Exception(filename + ": no such file")
        import_file(srcpath + "/" + filename, koocdata)


def import_file(filename, koocdata):
    imported = Kooc(filename)
    imported.koocdata = koocdata
    imported.parse_file(filename)
    koocdata = imported.koocdata
    return
