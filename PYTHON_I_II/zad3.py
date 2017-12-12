

import os

patch, dirs, files = os.walk("/dev").__next__()
file_count = len(files)

print(file_count)
