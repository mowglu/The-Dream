import re
import os
import time
import subprocess
from pathlib import Path


def treatWatermark(id='0', mydate='0', aircraftname='NA'):
    start_time = time.time()

    # Changing date to correct watermark format
    def month_converter(month):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        return months[month - 1]

    month = mydate[:2]
    changedmonth = month_converter(int(month))
    watermarkdate = mydate[3:5] + '-' + changedmonth + '-' + mydate[6:]

    # need to treat watermarked pdf to remove watermark
    mystr = os.path.dirname(os.path.realpath(__file__))
    mystr = Path(mystr)
    mystr = mystr.parent.parent.parent

    # mystr = "\"" + mystr + "\""
    entirecommand = f"\"{str(mystr)}\Part2\APG_Reports\\{id}.pdf\" output \"{str(mystr)}\Part2\APG_Reports\\uncompressed{id}.pdf\""
    subprocess.call(f"{str(mystr)}\Part2\PDFtk\\bin\pdftk.exe " + entirecommand + " uncompress")

    # input file
    _surrogates = re.compile(r"[\uDC80-\uDCFF]")

    def detect_decoding_errors_line(l, _s=_surrogates.finditer):
        """Return decoding errors in a line of text

        Works with text lines decoded with the surrogateescape
        error handler.

        Returns a list of (pos, byte) tuples
        """
        # DC80 - DCFF encode bad bytes 80-FF
        return [(m.start(), bytes([ord(m.group()) - 0xDC00]))
                for m in _s(l)]

    mystr = os.path.dirname(os.path.realpath(__file__))
    mystr = Path(mystr)
    mystr = mystr.parent.parent.parent

    fout = open(str(mystr) + '\Part2\APG_Reports\\uncompressed{}nomark.pdf'.format(id), "wt")

    with open(str(mystr) + '\Part2\APG_Reports\\uncompressed{}.pdf'.format(id), encoding="utf8",
              errors="surrogateescape") as f:
        for i, line in enumerate(f, 1):
            errors = detect_decoding_errors_line(line)
            if errors:
                pass
            else:
                fout.write(
                    line.replace('(Aircraft Performance Group, Inc)Tj', '( )Tj').replace("({})Tj".format(watermarkdate),
                                                                                         '( )Tj').replace(
                        '({})Tj'.format(aircraftname),
                        '( )Tj'))
    fout.close()

    mystr = os.path.dirname(os.path.realpath(__file__))
    mystr = Path(mystr)
    mystr = mystr.parent.parent.parent

    # mystr = "\"" + mystr + "\""
    entirecommand = f"\"{str(mystr)}\Part2\APG_Reports\\uncompressed{id}nomark.pdf\" output \"{str(mystr)}\Part2\APG_Reports\\treated{id}.pdf\""

    subprocess.call(f"{str(mystr)}\Part2\PDFtk\\bin\pdftk.exe " + entirecommand + " compress")

    # cleanup
    mystr = os.path.dirname(os.path.realpath(__file__))
    mystr = Path(mystr)
    mystr = mystr.parent.parent.parent

    entirecommand = str(mystr) + "\Part2\APG_Reports\\uncompressed{}nomark.pdf".format(id)
    os.remove(entirecommand)
    entirecommand = str(mystr) + "\Part2\APG_Reports\\uncompressed{}.pdf".format(id)
    os.remove(entirecommand)

    print("\n--- %s seconds to treat PDF ---\n" % (time.time() - start_time))
